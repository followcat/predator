# -*- coding: utf-8 -*-
import re
import time
import logging
import datetime
import functools

import precedure.jingying
import jobs.definition.cloudshare

from sources.industry_id import *
from jobs.config.jingying import *

class Jingying(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/jingying'
    FF_PROFILE_PATH = ff_profiles[0]
    PRECEDURE_CLASS = precedure.jingying.Jingying
    source = 'jingying'

    def cloudshare_yaml_template(self):
        template = super(Jingying, self).cloudshare_yaml_template()
        template['origin'] = u'无忧精英爬取'
        return template

    def simple_jobgenerator(self, industry_needed, keywords=None):
        start_time=datetime.datetime.now()
        for _classify_value in industry_needed:
            _classify_id = industryID[_classify_value.encode('utf-8')]
            _file = _classify_id + '.yaml'
            print('[jingying cv]: %s - %s'%(_classify_id, _classify_value))
            try:
                yamldata = self.get_cv_list(_file, keywords)
            except Exception:
                continue
            sorted_id = sorted(yamldata, key = lambda cvid: yamldata[cvid]['date'],
                               reverse=True)
            if sorted_id:
                print _file, sorted_id[0], time.localtime(yamldata[sorted_id[0]]['date'])
            for cv_id in sorted_id:
                if (time.time() - yamldata[cv_id]['date'])/60/60/24 < 14:
                    if not self.cvstorage.existscv(cv_id):
                        cv_info = yamldata[cv_id]
                        job_process = functools.partial(self.downloadjob, cv_info, _classify_id)
                        yield job_process
                        current_time = datetime.datetime.now()
                        duration=(current_time-start_time).seconds
                        if duration > 60:
                            time.sleep(10)
                            print '[jingying cv]: switch profile'
                            self.wb_downloader.switch_profile(ff_profiles)
                            start_time = current_time
                    else:
                        cv_info = yamldata[cv_id]
                        self.updatejob(cv_info)


    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        try:
            cv_content =  self.precedure.cv(cv_info['href'])
            yamldata = self.extract_details(cv_info, cv_content)
            result = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
            job_logger.info('Download: '+cv_id)
            print('[jingying cv]: Download: '+cv_id)
        except AttributeError as e:
            job_logger.error('Downloading: '+cv_id+ ' ' + e.message)
            print('[jingying cv]: Fails Download: '+cv_id)
            self.wb_downloader.switch_profile(ff_profiles)
            print('[jingying cv]: Switch Firefox profile!')

    def calculate_age(born):
        today = datetime.date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError:
            # raised when birth date is February 29 
            # and the current year is not a leap year
            birthday = born.replace(year=today.year, day=born.day-1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    def extract_details(self, uploaded_details, cv_content):
        details = super(Jingying, self).extract_details(uploaded_details)

        if not details['age']:
            re_born_date = u'(\d{4})年(\d{1,2})月(\d{1,2})日'
            regex = re.compile(re_born_date, re.IGNORECASE)
            res = re.findall(regex, cv_content)
            if len(res) > 0 and len(res[0]) == 3:
                age_res = res[0]
                try:
                    born = datetime.date(int(age_res[0]), int(age_res[1]), int(age_res[2]))
                    today = datetime.date.today()
                    try:
                        birthday = born.replace(year=today.year)
                    except ValueError:
                        birthday = born.replace(year=today.year, day=born.day-1)
                    if birthday > today:
                        age = today.year - born.year - 1
                    else:
                        age = today.year - born.year
                    if age >= 18:
                        details['age'] = age
                except ValueError:
                    pass

        if not details['tags']:
            details['tags'] = uploaded_details['tags']

        return details

