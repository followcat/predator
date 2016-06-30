# -*- coding: utf-8 -*-
import Queue
import functools

import utils.builtin
import jobs.definition.cloudshare_zhilian
from jobs.definition.batchconvert import *


class Batchconvert(BatchconvertCloudshare,
                   jobs.definition.cloudshare_zhilian.Zhilian):

    CVDB_PATH = 'convert/zhilian'
    ORIGIN_CVDB_PATH = 'zhilian_cv'

    def jobgenerator(self, classify_id_list):
        for classify_id in classify_id_list:
            yamlname = classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('zhilian/JOBTITLES', yamlname)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if self.oristorage.exists(cv_id) and not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.convertjob, cv_info)
                    yield job_process


if __name__ == '__main__':
    industry_yamls = ['160000', ##计算机/网络技术
                      '249', ##质量管理/测试经理(QA/QC经理)(质量管理/安全防护)
                      '250', ##质量管理/测试主管(QA/QC主管)(质量管理/安全防护)
                      '251', ##质量管理/测试工程师(QA/QC工程师)(质量管理/安全防护)
                      '732', ##机电工程师(工程机械)
                      '410', ##测试/可靠性工程师(电子/电气/半导体/仪器仪表)
                      '84' ##FAE现场应用工程师(电子/电气/半导体/仪器仪表)
                     ]
    instance = Batchconvert()
    PROCESS_GEN = instance.jobgenerator(industry_yamls)

    queue_saver = Queue.Queue(0)
    t1 = ThreadConverter('1', queue_saver, PROCESS_GEN)
    t2 = ThreadConverter('2', queue_saver, PROCESS_GEN)
    t3 = ThreadConverter('3', queue_saver, PROCESS_GEN)
    t4 = ThreadConverter('4', queue_saver, PROCESS_GEN)

    saver = ThreadSaver('saver', queue_saver, instance.cvstorage)

    saver.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
