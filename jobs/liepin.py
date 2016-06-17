import logging
import functools

import tools.log

import utils.builtin
import precedure.liepin

import storage.repocv
import storage.gitinterface
import downloader.webdriver


CVDB_PATH = 'liepin_webdrivercv'
FF_PROFILE_PATH = '/home/followcat/.mozilla/firefox/yffp11op.followcat'
PRECEDURE_CLASS = precedure.liepin.Liepin

wb_downloader = downloader.webdriver.Webdriver(FF_PROFILE_PATH)
liepin_pre = PRECEDURE_CLASS(wbdownloader=wb_downloader)
cvrepo = storage.gitinterface.GitInterface(CVDB_PATH)
cvstorage = storage.repocv.CurriculumVitae(cvrepo)

PLAN = [dict(minute='*/5', hour='8-17'),
        dict(minute='*/15', hour='18-23'),
        dict(minute='*/15', hour='0-2')]

def jobgenerator(precedure, cvstorage):

    def downloadjob(cv_info, precedure, cvstorage):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        cv_content =  precedure.cv(cv_info['href'])
        result = cvstorage.add(cv_id, cv_content.encode('utf-8'), 'followcat')
        print('Download: '+cv_id)
        job_logger.info('Download: '+cv_id)
        result = True

    yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
    sorted_id = sorted(yamldata,
                       key = lambda cvid: yamldata[cvid]['peo'][-1],
                       reverse=True)
    for cv_id in sorted_id:
        if not cvstorage.exists(cv_id):
            cv_info = yamldata[cv_id]
            job_process = functools.partial(downloadjob, cv_info, precedure, cvstorage)
            yield job_process

PROCESS_GEN = jobgenerator(liepin_pre, cvstorage)
