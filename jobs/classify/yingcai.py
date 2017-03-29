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
    source = 'yingcai'
    precedure_type = precedure.yingcai.Yingcai
    wbdownloader = True
    cookies_file = None

    def industryjob(self, industryid, filename, industry, keywords=None, resume=False):
        start_time=datetime.datetime.now()
        if keywords is None or len(keywords) == 0:
            keywords = ['']
        print start_time
        for keyword in keywords:
            for index in industry:
                industry_id = index[0]
                industry_value = index[1]
                postinfo = {
                            'industrys': industry_value,
                            'searchtext': keyword,
                            }
                getdict = {
                        'wishIndustry':industry_id,
                        'page':'0',
                        'keyword': keyword
                        }
                for key, value in job_list.items():
                    if not key.startswith(industry_id):
                        continue
                    if keyword != '':
                        print '爬取行业：{0}:{1}'.format(industry_id, industry_value)
                        print u'爬取关键词：{0}'.format(keyword)
                    else:
                        print '爬取行业：{0}:{1}'.format(industry_id, industry_value)
                        print '爬取职位：{0}:{1}'.format(key, value)
                        getdict['jobs'] = key
                        postinfo['jobtitles'] = value
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
                            self.downloader.switch_profile(FF_PROFILE_PATH_LIST)
                        start_time = current_time
                    if keyword != '':
                        break

    def autologin(self):
        self.precedure.login(self.username, self.password)

repo = storage.fsinterface.FSInterface('output/yingcai')

PLAN = [dict(name='yingcai_classify', second='*/60', hour='8-19'),
        dict(name='yingcai_classify', minute='*/5', hour='20-23'),
        dict(name='yingcai_classify', minute='*/10', hour='0-7')]

def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = Yingcai(repo, downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC
