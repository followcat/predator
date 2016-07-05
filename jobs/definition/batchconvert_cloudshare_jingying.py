import Queue
import functools

import utils.builtin
import jobs.definition.cloudshare_jingying
from jobs.definition.batchconvert import *


class Batchconvert(BatchconvertCloudshare,
                   jobs.definition.cloudshare_jingying.Jingying):

    CVDB_PATH = 'convert/jingying'
    ORIGIN_CVDB_PATH = 'output/jingying'

    def jobgenerator(self, idlist):
        for classify_id in idlist:
            yamlname = classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', yamlname)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if self.oristorage.existsraw(cv_id) and not self.cvstorage.existscv(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.convertjob, cv_info)
                    yield job_process

    def extract_details(self, uploaded_details, cv_content):
        details = super(Batchconvert, self).extract_details(uploaded_details, cv_content)
        details['date'] = uploaded_details['date']
        return details


if __name__ == '__main__':
    industry_yamls = jobs.definition.cloudshare_jingying.industry_yamls
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
