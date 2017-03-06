# encoding: utf-8

import time
import datetime
import functools

import precedure.yingcai
import storage.fsinterface
import jobs.classify.base

import jobs.config.yingcai
from sources.yingcai_job import *



FF_PROFILE_PATH_LIST = jobs.config.yingcai.ff_profiles

class Yingcai(jobs.classify.base.Base):

    profilepath_index = 0
    FF_PROFILE_PATH = FF_PROFILE_PATH_LIST[profilepath_index]
    ff_profile = FF_PROFILE_PATH

    ACCOUNT_LIST=jobs.config.yingcai.accounts
    username, password = ACCOUNT_LIST[0]

    jobname = 'yingcai'
    precedure_type = precedure.yingcai.Yingcai
    wbdownloader = True
    cookies_file = None

    def industryjob(self, industryid, filename, industry, resume=False):
        start_time=datetime.datetime.now()
        print start_time
        for index in industry:
            industry_id = index[0]
            industry_value = index[1]
            for key, value in job_list.items():
                if not key.startswith(industry_id):
                    continue
                postinfo = {
                            'industrys': industry_value,
                            'jobtitles': value,
                            }
                print '爬取行业：{0}:{1}'.format(industry_id, industry_value)
                print '爬取职位：{0}:{1}'.format(key, value)
                getdict = {
                        'jobs':key,
                        'wishIndustry':industry_id,
                        'page':'0'
                        }
                header = self.gen_header(getdict, postinfo)
                #import ipdb;ipdb.set_trace()
                #print "header:",header
                if resume and not self.eq_postdict(industryid, getdict,
                                                   exclude=[self.precedure.PAGE_VAR]):
                    continue
                else:
                    resume = False
                job_process = functools.partial(self.precedure.update_classify,
                                                filename, filename,
                                                getdict, self.repojt, header)
                yield job_process
                current_time = datetime.datetime.now()
                duration=(current_time-start_time).seconds
                if duration > 1800:
                    time.sleep(10)
                    if hasattr(self, 'login') and self.login is True:
                        print 'login again'
                        accountlist_index = self.ACCOUNT_LIST.index((self.username, self.password))
                        accountlist_index = (accountlist_index+1)%len(self.ACCOUNT_LIST)
                        self.username, self.password = self.ACCOUNT_LIST[accountlist_index]
                        self.autologin()
                    else:
                        print 'switch profile'
                        self.wb_downloader.switch_profile(self.FF_PROFILE_PATH_LIST)
                    start_time = current_time

    def autologin(self):
        self.precedure.login(self.username, self.password)


repo = storage.fsinterface.FSInterface('output/yingcai')
instance = Yingcai(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/60', hour='8-17'),
        dict(second='*/60', hour='18-23'),
        dict(second='*/60', hour='0-7')]
