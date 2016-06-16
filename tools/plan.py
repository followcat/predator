import os
import time
import random
import logging

import tools.log
import tools.mail
import utils.builtin
import precedure.liepin
import storage.repocv
import storage.gitinterface
import downloader.webdriver

import apscheduler.events
import apscheduler.schedulers.blocking

scheduler = apscheduler.schedulers.blocking.BlockingScheduler()

cvrepo = storage.gitinterface.GitInterface('liepin_webdrivercv')
cv = storage.repocv.CurriculumVitae(cvrepo)
wb_downloader = downloader.webdriver.Webdriver(
                    '/home/followcat/.mozilla/firefox/yffp11op.followcat')
liepin_pre = precedure.liepin.Liepin(wbdownloader=wb_downloader)


def tick(cvid_gen, yamldata):
    result = False
    nums_tensec = random.randint(0, 18)
    time.sleep(nums_tensec*10)
    job_logger = logging.getLogger('schedJob')
    print('Tick! The time is: %s' % time.ctime())
    cv_id = cvid_gen.next()
    while cv.exists(cv_id):
        cv_id = cvid_gen.next()
    cv_info = yamldata[cv_id]
    cv_content =  liepin_pre.cv(cv_info['href'])
    result = cv.add(cv_id, cv_content.encode('utf-8'), 'followcat')
    print('Download: '+cv_id)
    job_logger.info('Download: '+cv_id)
    result = True
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


if __name__ == '__main__':
    yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
    sorded_id = sorted(yamldata,
                       key = lambda cvid:yamldata[cvid]['peo'][-1],
                       reverse=True)
    cvid_gen = iter(sorded_id)
    scheduler.add_job(tick, 'cron', minute='*/5', hour='8-17', args=[cvid_gen, yamldata])
    scheduler.add_job(tick, 'cron', minute='*/15', hour='18-23', args=[cvid_gen, yamldata])
    scheduler.add_job(tick, 'cron', minute='*/15', hour='0-2', args=[cvid_gen, yamldata])
    scheduler.add_listener(err_listener,
        apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED) 
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
