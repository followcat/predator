import os
import time
import random
import logging

import tools.log
import tools.mail

import apscheduler.events
import apscheduler.schedulers.blocking

scheduler = apscheduler.schedulers.blocking.BlockingScheduler()


def randomjob(cvinfo_gen, precedure, cvstorage):
    result = False
    nums_tensec = random.randint(0, 18)
    time.sleep(nums_tensec*10)
    job_logger = logging.getLogger('schedJob')
    print('The time is: %s' % time.ctime())
    cv_info = cvinfo_gen.next()
    cv_id = cv_info['id']
    cv_content =  precedure.cv(cv_info['href'])
    result = cvstorage.add(cv_id, cv_content.encode('utf-8'), 'followcat')
    print('Download: '+cv_id)
    job_logger.info('Download: '+cv_id)
    result = True
    return result


def jobgenerator(yamldata, cvstorage):
    sorted_id = sorted(yamldata,
                       key = lambda cvid:yamldata[cvid]['peo'][-1],
                       reverse=True)
    for cv_id in sorted_id:
        if not cvstorage.exists(cv_id):
            yield yamldata[cv_id]


def err_listener(ev):
    err_logger = logging.getLogger('schedErrJob')
    if ev.exception:
        err_logger.error('%s error.', str(ev.job_id))
    else:
        err_logger.info('%s miss', str(ev.job_id))
    tools.mail.send_mail(['fengliji@willendare.com'], ev.job_id, "Wrong and stop!")
    global scheduler
    scheduler.shutdown()


if __name__ == '__main__':
    import utils.builtin
    import precedure.liepin
    import storage.repocv
    import storage.gitinterface
    import downloader.webdriver
    yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
    wb_downloader = downloader.webdriver.Webdriver(
                        '/home/followcat/.mozilla/firefox/yffp11op.followcat')
    liepin_pre = precedure.liepin.Liepin(wbdownloader=wb_downloader)
    cvrepo = storage.gitinterface.GitInterface('liepin_webdrivercv')
    cvstorage = storage.repocv.CurriculumVitae(cvrepo)

    cvinfo_gen = jobgenerator(yamldata, cvstorage)
    scheduler.add_job(randomjob, 'cron', minute='*/5', hour='8-17',
                      args=[cvinfo_gen, liepin_pre, cvstorage])
    scheduler.add_job(randomjob, 'cron', minute='*/15', hour='18-23',
                      args=[cvinfo_gen, liepin_pre, cvstorage])
    scheduler.add_job(randomjob, 'cron', minute='*/15', hour='0-2',
                      args=[cvinfo_gen, liepin_pre, cvstorage])
    scheduler.add_listener(err_listener,
        apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED) 
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
