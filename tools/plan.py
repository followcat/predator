import os
import sys
import time
import random
import logging
import functools

import tools.log
import tools.mail

import apscheduler.events
import apscheduler.schedulers.blocking

scheduler = apscheduler.schedulers.blocking.BlockingScheduler()


def randomjob(process_gen, sleep=True):
    result = False
    if sleep is True:
        nums_tensec = random.randint(0, 18)
        time.sleep(nums_tensec*10)
    print('The time is: %s' % time.ctime())
    job_process = process_gen.next()
    result = job_process()
    return result


def err_listener(ev):
    err_logger = logging.getLogger('schedErrJob')
    if ev.exception:
        err_logger.error('%s error.', str(ev.job_id))
    else:
        err_logger.info('%s miss', str(ev.job_id))
    tools.mail.send_mail(['fengliji@willendare.com'], ev.job_id, "Wrong and stop!")
    global scheduler
    scheduler.shutdown()


def downloadjob(cv_info, precedure, cvstorage):
    job_logger = logging.getLogger('schedJob')
    cv_id = cv_info['id']
    cv_content =  precedure.cv(cv_info['href'])
    result = cvstorage.add(cv_id, cv_content.encode('utf-8'), 'followcat')
    print('Download: '+cv_id)
    job_logger.info('Download: '+cv_id)
    result = True


def jobgenerator(yamldata, precedure, cvstorage, sortfunc):
    sorted_id = sorted(yamldata,
                       key = sortfunc,
                       reverse=True)
    for cv_id in sorted_id:
        if not cvstorage.exists(cv_id):
            cv_info = yamldata[cv_id]
            job_process = functools.partial(downloadjob, cv_info, precedure, cvstorage)
            yield job_process


def jobadder(scheduler, job, plan, arguments=None, kwarguments=None):
    if arguments is None:
        arguments = []
    if kwarguments is None:
        kwarguments = {}
    for each in plan:
        scheduler.add_job(job, 'cron', args=arguments, kwargs=kwarguments, **each)


if __name__ == '__main__':
    import importlib
    jobmodule_name = sys.argv[1]
    jobmodule = importlib.import_module(jobmodule_name)
    CVDB_PATH = jobmodule.CVDB_PATH
    FF_PROFILE_PATH = jobmodule.FF_PROFILE_PATH
    PRECEDURE_CLASS = jobmodule.PRECEDURE_CLASS
    YAMLDATA = jobmodule.YAMLDATA
    PLAN = jobmodule.PLAN
    SORTFUNC = jobmodule.SORTFUNC

    import storage.repocv
    import storage.gitinterface
    import downloader.webdriver
    yamldata = YAMLDATA
    wb_downloader = downloader.webdriver.Webdriver(FF_PROFILE_PATH)
    liepin_pre = PRECEDURE_CLASS(wbdownloader=wb_downloader)
    cvrepo = storage.gitinterface.GitInterface(CVDB_PATH)
    cvstorage = storage.repocv.CurriculumVitae(cvrepo)

    process_gen = jobgenerator(yamldata, liepin_pre, cvstorage, SORTFUNC)
    jobadder(scheduler, randomjob, PLAN,
             arguments=[process_gen],
             kwarguments=dict(sleep=True))
    scheduler.add_listener(err_listener,
        apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED) 
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
