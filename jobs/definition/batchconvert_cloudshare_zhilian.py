# -*- coding: utf-8 -*-

import yaml
import time
import Queue
import functools
import threading

import utils.builtin
import storage.cv
import storage.jobtitles
import storage.fsinterface
import storage.gitinterface
import jobs.definition.cloudshare_zhilian


class Batchconvert(jobs.definition.cloudshare_zhilian.Zhilian):

    CVDB_PATH = 'convert/zhilian'
    ORIGIN_CVDB_PATH = 'zhilian_cv'

    def __init__(self):
        self.gitinterface = storage.gitinterface.GitInterface(self.ORIGIN_CVDB_PATH)
        self.oristorage = storage.cv.CurriculumVitae(self.gitinterface)

        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtstorage = storage.jobtitles.JobTitles(self.fsinterface)

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

    def convertjob(self, cv_info):
        cv_id = cv_info['id']
        cv_content =  self.oristorage.get(cv_info['id'])
        yamldata = self.extract_details(cv_info, cv_content)
        return cv_content, yamldata


class ThreadConverter(threading.Thread):

    def __init__(self, name, queue, process_gen):
        super(ThreadConverter, self).__init__()
        self.name = name
        self.queue = queue
        self.process_gen = process_gen
        self.setDaemon(True)

    def run(self):
        while True:
            try:
                process_job = self.process_gen.next()
            except ValueError:
                time.sleep(0.1)
                continue
            except StopIteration:
                break
            cv_content, summary = process_job()
            self.queue.put((cv_content, summary))


class ThreadSaver(threading.Thread):

    def __init__(self, name, queue, cvstorage, jtstorage):
        super(ThreadSaver, self).__init__()
        self.name = name
        self.queue = queue
        self.cvstorage = cvstorage
        self.jtstorage = jtstorage

    def run(self):
        count = 0
        while True:
            cv_content, summary = self.queue.get()
            count += 1
            print(count, summary['id'])
            cv_id = summary['id']
            self.cvstorage.add(cv_id, cv_content)
            self.jtstorage.add_data(cv_id, summary)


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

    saver = ThreadSaver('saver', queue_saver, instance.cvstorage, instance.jtstorage)

    saver.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
