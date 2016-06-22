import time
import Queue
import functools
import threading

import utils.builtin
import storage.cv
import storage.jobtitles
import storage.fsinterface
import storage.gitinterface
import jobs.definition.cloudshare_liepin


class Batchconvert(jobs.definition.cloudshare_liepin.Liepin):

    CVDB_PATH = 'output/liepin'
    ORIGIN_CVDB_PATH = 'liepin_webdrivercv'

    def __init__(self):
        self.gitinterface = storage.gitinterface.GitInterface(self.ORIGIN_CVDB_PATH)
        self.oristorage = storage.cv.CurriculumVitae(self.gitinterface)

        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtstorage = storage.jobtitles.JobTitles(self.fsinterface)

    def jobgenerator(self, classify_id):
        self.classify_id = classify_id
        yamlname = classify_id + '.yaml'
        yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', yamlname)
        sorted_id = sorted(yamldata,
                           key = lambda cvid: yamldata[cvid]['peo'][-1],
                           reverse=True)
        for cv_id in sorted_id:
            if self.oristorage.exists(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.downloadjob, cv_info)
                yield job_process

    def downloadjob(self, cv_info):
        cv_id = cv_info['id']
        cv_content =  self.oristorage.get(cv_info['id'])
        cvresult = self.cvstorage.add(cv_id, cv_content)
        yamldata = self.extract_details(cv_info)
        return yamldata


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
                print process_job
            except ValueError:
                time.sleep(0.1)
                continue
            except StopIteration:
                break
            result = process_job()
            self.queue.put(result)
            print(self.name, result['id'])


class ThreadSaver(threading.Thread):

    def __init__(self, name, queue):
        super(ThreadSaver, self).__init__()
        self.name = name
        self.queue = queue
        self.yamldata = {}
        self.setDaemon(True)

    def run(self):
        while True:
            single_yamldata = self.queue.get()
            cvid = single_yamldata['id']
            self.yamldata[cvid] = single_yamldata


if __name__ == '__main__':
    instance = Batchconvert()
    PROCESS_GEN = instance.jobgenerator('290097')

    queue_saver = Queue.Queue(0)
    t1 = ThreadConverter('1', queue_saver, PROCESS_GEN)
    t2 = ThreadConverter('2', queue_saver, PROCESS_GEN)
    t3 = ThreadConverter('3', queue_saver, PROCESS_GEN)
    t4 = ThreadConverter('4', queue_saver, PROCESS_GEN)

    saver = ThreadSaver('saver', queue_saver)

    saver.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
