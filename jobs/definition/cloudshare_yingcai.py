# -*- coding: utf-8 -*-
import re
import bs4
import time
import datetime
import logging
import datetime
import functools

import utils.builtin
import precedure.yingcai
import jobs.definition.cloudshare

import jobs.config.yingcai
from sources.industry_id import *

class Yingcai(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/yingcai'
    FF_PROFILE_PATH_LIST = jobs.config.yingcai.ff_profiles
    profilepath_index = 0
    FF_PROFILE_PATH = FF_PROFILE_PATH_LIST[profilepath_index]

    ACCOUNT_LIST=jobs.config.yingcai.accounts
    username, password = ACCOUNT_LIST[0]

    PRECEDURE_CLASS = precedure.yingcai.Yingcai
    START_TIME=datetime.datetime.now()
    source = 'yingcai'

    def cloudshare_yaml_template(self):
        template = super(Yingcai, self).cloudshare_yaml_template()
        template['origin'] = u'中华英才爬取'
        return template

    def simple_jobgenerator(self, industry_needed, keywords=None):
        for _classify_value in industry_needed:
            _classify_id = industryID[_classify_value.encode('utf-8')]
            print('[yingcai cv]: %s'%_classify_id)
            _file = _classify_id + '.yaml'
            try:
                yamldata = self.get_cv_list(_file, keywords)
            except Exception:
                continue
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['info'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if not self.cvstorage.existscv(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info, _classify_id)
                    t1 = time.time()
                    yield job_process

                current_time=datetime.datetime.now()
                duration=(current_time-self.START_TIME).seconds
                if duration > 1800:
                    #Wait for job done, then login again or switch user
                    time.sleep(10)
                    if hasattr(self, 'login') and self.login is True:
                        print('[yingcai cv]: login again')
                        accountlist_index = self.ACCOUNT_LIST.index((self.username, self.password))
                        accountlist_index = (accountlist_index+1)%len(self.ACCOUNT_LIST)
                        self.username, self.password = self.ACCOUNT_LIST[accountlist_index]
                        self.autologin()
                    else:
                        print('[yingcai cv]: switch user')
                        self.wb_downloader.switch_profile(self.FF_PROFILE_PATH_LIST)
                    self.START_TIME = current_time

    def autologin(self):
        self.precedure.login(self.username, self.password)

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('[yingcai cv]: Download: '+cv_id)
        print('[yingcai cv]: %s'%cv_info['href'])
        cv_content =  self.precedure.cv(cv_info['href'])
        yamldata = self.extract_details(cv_info, cv_content)
        result = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
        job_logger.info('Download: '+cv_id)
        result = True

    def extract_details(self, uploaded_details, cv_content):
        details = super(Yingcai, self).extract_details(uploaded_details)
        soup=bs4.BeautifulSoup(cv_content,'lxml')

        if not details['name']:
            name = uploaded_details['name']
            if len(name) == 0:
                details['name'] = uploaded_details['id']
            else:
                details['name'] = uploaded_details['name']

        if not details['age']:
            age = uploaded_details['info'][0]
            age_pattern = re.compile(r'(\d+)')
            details['age'] = int(re.findall(age_pattern, age)[0])

        if not details['education']:
            details['education'] = uploaded_details['info'][2].strip()

        if not details['tags']:
            details['tags'] = uploaded_details['tags']
        
        return details
