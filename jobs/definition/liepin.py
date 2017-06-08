import functools

import utils.builtin
import precedure.liepin
import jobs.definition.base


class Liepin(jobs.definition.base.Base):

    CVDB_PATH = 'liepin_webdrivercv'
    FF_PROFILE_PATH = '/home/followcat/.mozilla/firefox/yffp11op.followcat'
    PRECEDURE_CLASS = precedure.liepin.Liepin

    def jobgenerator(self):
        yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
        if 'datas' in yamldata:
            yamldata = yamldata['datas']
        sorted_id = sorted(yamldata, key = lambda cvid: yamldata[cvid]['date'],
                           reverse=True)
        for cv_id in sorted_id:
            if not self.cvstorage.exists(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.downloadjob, cv_info)
                yield job_process
