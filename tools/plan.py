import os
import time
import datetime 

import utils.builtin
import htmlparser.liepin
import downloader.liepin
import storage.repocv
import storage.gitinterface
import storage.repojobtitles

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

jtrepo = storage.gitinterface.GitInterface('liepin')
jt = storage.repojobtitles.JobTitles(jtrepo)
cvrepo = storage.gitinterface.GitInterface('liepin_webdrivercv')
cv = storage.repocv.CurriculumVitae(cvrepo)
downloader = downloader.liepin.Webdriver('/home/followcat/.mozilla/firefox/yffp11op.followcat')


def tick():
    job_logger = logging.getLogger('schedJob')
    print('Tick! The time is: %s' % datetime.datetime.now())
    yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', '290094.yaml')
    for cv_id in yamldata:
        if cv.exists(cv_id):
            continue
        cv_info = yamldata[cv_id]
        cv_url = cv_info['href']
        htmlsource = downloader.cv(cv_url)
        cv_content = htmlparser.liepin.catchcv(htmlsource)
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
    global scheduler
    scheduler.shutdown()


if __name__ == '__main__':
    scheduler.add_job(tick, 'cron', minute='*/3', day_of_week='4-6', hour='9-22')
    scheduler.add_listener(err_listener,
        apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED) 
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
