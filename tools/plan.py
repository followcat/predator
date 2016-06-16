import os
import time
import random

import tools.mail
import utils.builtin
import precedure.liepin
import storage.repocv
import storage.gitinterface
import downloader.webdriver

import apscheduler.events
import apscheduler.schedulers.blocking

import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='plan.log',
                filemode='a')

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='plan.log',
                filemode='a')

logging.basicConfig(level=logging.ERROR,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='plan.log',
                filemode='a')

scheduler = apscheduler.schedulers.blocking.BlockingScheduler()

cvrepo = storage.gitinterface.GitInterface('liepin_webdrivercv')
cv = storage.repocv.CurriculumVitae(cvrepo)
wb_downloader = downloader.webdriver.Webdriver(
                    '/home/followcat/.mozilla/firefox/yffp11op.followcat')
liepin_pre = precedure.liepin.Liepin(wbdownloader=wb_downloader)


def tick():
    nums_tensec = random.randint(0, 18)
    time.sleep(nums_tensec*10)
    job_logger = logging.getLogger('schedJob')
    print('Tick! The time is: %s' % time.ctime())
    yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')
    sorded_id = sorted(yamldata,
                       key = lambda cvid:yamldata[cvid]['peo'][-1],
                       reverse=True)
    for cv_id in sorded_id:
        if cv.exists(cv_id):
            continue
        cv_info = yamldata[cv_id]
        cv_url = cv_info['href']
        download_url = 'https://h.liepin.com' + cv_url
        cv_content =  liepin_pre.cv(download_url)
        result = cv.add(cv_id, cv_content.encode('utf-8'), 'followcat')
        print('Download: '+cv_id)
        job_logger.info('Download: '+cv_id)
        break
    return True


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
    scheduler.add_job(tick, 'cron', minute='*/5', hour='8-17')
    scheduler.add_job(tick, 'cron', minute='*/15', hour='18-23')
    scheduler.add_job(tick, 'cron', minute='*/15', hour='0-2')
    scheduler.add_listener(err_listener,
        apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED) 
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
