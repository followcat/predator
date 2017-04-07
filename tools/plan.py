import os
import time
import random
import logging
import inspect
import argparse
import importlib

import apscheduler.events
import apscheduler.schedulers.blocking

scheduler = apscheduler.schedulers.blocking.BlockingScheduler()

NOLOGINRETRYWAIT = 1200


def schedulerjob(process_gen, sleep=True):
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
    global scheduler
    if ev.exception:
        err_logger.error('%s error.', str(ev.job_id))
        if ev.exception.message == 'NoLoginError':
            err_job = scheduler.get_job(ev.job_id)
            jobs = [j for j in scheduler.get_jobs() if j.name==err_job.name]
            for job in jobs:
                scheduler.pause_job(job.id)
                print('pause job %s'%str(job))
            time.sleep(NOLOGINRETRYWAIT)
            for job in jobs:
                scheduler.resume_job(job.id)
                print('resume job %s'%str(job))
    else:
        err_logger.info('%s miss', str(ev.job_id))

def jobadder(scheduler, job, plan, arguments=None, kwarguments=None):
    if arguments is None:
        arguments = []
    if kwarguments is None:
        kwarguments = {}
    for each in plan:
        scheduler.add_job(job, 'cron', args=arguments, kwargs=kwarguments, **each)

parser = argparse.ArgumentParser(description='Plan tool.')
parser.add_argument('--jobs', type=str, help='Process job generateor module.')
parser.add_argument('--config', type=str, default='', help='Configure file')
parser.add_argument('-r', '--resume', action='store_true', help='Let resume be True.')

if __name__ == '__main__':
    
    args = parser.parse_args()
    jobs = args.jobs.split(',')
    config = args.config
    print jobs
    downloaders = {}
    for job in jobs:
        jobmodule = importlib.import_module(job)
        PLAN = jobmodule.PLAN
        if hasattr(jobmodule, 'PROCESS_GEN_FUNC'):
            PROCESS_GEN_FUNC = jobmodule.PROCESS_GEN_FUNC
        else:
            PROCESS_GEN_FUNC = jobmodule.get_PROCESS_GEN_FUNC(downloaders)
        if 'resume' in inspect.getargspec(PROCESS_GEN_FUNC).args:
            PROCESS_GEN = PROCESS_GEN_FUNC(config, resume=args.resume)
        else:
            PROCESS_GEN = PROCESS_GEN_FUNC(config)

        jobadder(scheduler, schedulerjob, PLAN,
                 arguments=[PROCESS_GEN],
                 kwarguments=dict(sleep=False))
        scheduler.add_listener(err_listener,
            apscheduler.events.EVENT_JOB_ERROR | apscheduler.events.EVENT_JOB_MISSED)
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        if not scheduler.running:
            scheduler.start()
    except (KeyboardInterrupt, SystemExit) as e:
        raise e
        scheduler.shutdown()
