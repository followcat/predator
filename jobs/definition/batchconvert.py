import time
import threading

import utils.builtin
import storage.cv
import storage.fsinterface
import jobs.definition.cloudshare


class Batchconvert(object):

    CVDB_PATH = 'convert/name'
    ORIGIN_CVDB_PATH = 'output/name'

    def __init__(self):
        self.oriinterface = storage.fsinterface.FSInterface(self.ORIGIN_CVDB_PATH)
        self.oristorage = storage.cv.CurriculumVitae(self.oriinterface)

        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)


class BatchconvertCloudshare(Batchconvert,
                             jobs.definition.cloudshare.Cloudshare):

    def convertjob(self, cv_info):
        cv_id = cv_info['id']
        cv_content =  self.oristorage.getraw(cv_info['id'])
        yamldata = self.extract_details(cv_info)
        return cv_content, yamldata

    def jobgenerator(self, classify_path):
        yamldata = {}
        for f in glob.glob(os.path.join(classify_path, '*.yaml')):
            path, name = os.path.split(f)
            singledata = utils.builtin.load_yaml(path, name)
            yamldata.update(singledata)
        sorted_id = sorted(yamldata,
                           key = lambda cvid: yamldata[cvid]['peo'][-1],
                           reverse=True)
        for cv_id in sorted_id:
            if self.oristorage.existscv(cv_id) and not self.cvstorage.existscv(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.convertjob, cv_info)
                yield job_process


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

    def __init__(self, name, queue, cvstorage):
        super(ThreadSaver, self).__init__()
        self.name = name
        self.queue = queue
        self.cvstorage = cvstorage

    def run(self):
        count = 0
        while True:
            cv_content, summary = self.queue.get()
            count += 1
            print(count, summary['id'])
            cv_id = summary['id']
            self.cvstorage.addcv(cv_id, cv_content, summary)
