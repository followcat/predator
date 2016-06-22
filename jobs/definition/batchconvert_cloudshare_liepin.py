import functools

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
        self.save_yamldatas = []

    def jobgenerator(self, classify_id):
        self.save_yamldatas = []
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
        print('Convert: '+cv_id)
        cv_content =  self.oristorage.get(cv_info['id'])
        cvresult = self.cvstorage.add(cv_id, cv_content)
        yamldata = self.extract_details(cv_info)
        self.save_yamldatas.append(yamldata)
        result = True

    def save(self):
        self.jtstorage.add_datas(self.classify_id, self.save_yamldatas)

if __name__ == '__main__':
    instance = Batchconvert()
    PROCESS_GEN = instance.jobgenerator('290097')
    for p in PROCESS_GEN:
        p()
    instance.save()
