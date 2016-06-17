import functools

import jobs.base
import utils.builtin
import precedure.liepin


class Liepin(jobs.base.Base):

    CVDB_PATH = 'liepin_webdrivercv'
    FF_PROFILE_PATH = '/home/followcat/.mozilla/firefox/yffp11op.followcat'
    PRECEDURE_CLASS = precedure.liepin.Liepin

    def jobgenerator(self):
        yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
        sorted_id = sorted(yamldata,
                           key = lambda cvid: yamldata[cvid]['peo'][-1],
                           reverse=True)
        for cv_id in sorted_id:
            if not self.cvstorage.exists(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.downloadjob, cv_info)
                yield job_process

instance = Liepin()

PROCESS_GEN = instance.jobgenerator()
PLAN = [dict(minute='*/5', hour='8-17'),
        dict(minute='*/15', hour='18-23'),
        dict(minute='*/15', hour='0-2')]
