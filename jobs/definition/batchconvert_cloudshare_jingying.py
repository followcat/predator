# -*- coding: utf-8 -*-
import time
import Queue
import functools
import threading

import utils.builtin
import storage.cv
import storage.jobtitles
import storage.fsinterface
import jobs.definition.cloudshare_jingying


class Batchconvert(jobs.definition.cloudshare_jingying.Jingying):

    CVDB_PATH = 'convert/jingying'
    #CVDB_PATH = 'additional/jingying'
    ORIGIN_CVDB_PATH = 'jingying_webdrivercv'

    def __init__(self):
        self.orinterface = storage.fsinterface.FSInterface(self.ORIGIN_CVDB_PATH)
        self.oristorage = storage.cv.CurriculumVitae(self.orinterface)

        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtstorage = storage.jobtitles.JobTitles(self.fsinterface)
        self.save_yamldatas = []

    def jobgenerator(self, idlist):
        for classify_id in idlist:
            self.save_yamldatas = []
            yamlname = classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', yamlname)
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
        print('Convert: '+cv_id)
        cv_content =  self.oristorage.get(cv_info['id'])
        yamldata = self.extract_details(cv_info, cv_content)
        return cv_content, yamldata


class ThreadConverter(threading.Thread):

    def __init__(self, name, queue, process_gen):
        super(ThreadConverter, self).__init__()
        self.name = name
        self.queue = queue
        self.process_gen = process_gen

    def run(self):
        while True:
            try:
                process_job = self.process_gen.next()
            except ValueError:
                time.sleep(0.1)
                continue
            except StopIteration as e:
                print(e)
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
        self.yamldata = {}
        self.setDaemon(True)

    def run(self):
        count = 0
        while True:
            cv_content, summary = self.queue.get()
            count += 1
            cv_id = summary['id']
            print(count, cv_id)
            self.cvstorage.add(cv_id, cv_content)
            self.jtstorage.add_data(cv_id, summary)


if __name__ == '__main__':
    industry_yamls = jobs.definition.cloudshare_jingying.industry_yamls
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
