# -*- coding: utf-8 -*-
import re
import time
import logging
import datetime
import functools

import utils.builtin
import precedure.jingying
import jobs.definition.cloudshare

from sources.industry_id import *

class Jingying(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/jingying'
    FF_PROFILE_PATH = '/home/jeff/.mozilla/firefox/16xuwjcx.51jingying_2'
    FF_PROFILE_PATH_BACKUPS = [
        '/home/jeff/.mozilla/firefox/u2ip99rl.flj_jingying',
        '/home/jeff/.mozilla/firefox/2mkrz29h.jingying_chunjing',
        '/home/jeff/.mozilla/firefox/8xjhortl.jingying_jingwen',
        ]
    PRECEDURE_CLASS = precedure.jingying.Jingying

    def cloudshare_yaml_template(self):
        template = super(Jingying, self).cloudshare_yaml_template()
        template['origin'] = u'无忧精英爬取'
        return template

    def jobgenerator(self, industry_needed):
        for _classify_value in industry_needed:
            _classify_id = industryID[_classify_value.encode('utf-8')]
            _file = _classify_id + '.yaml'
            print('%s - %s'%(_classify_id, _classify_value))
            try:
                yamlfile = utils.builtin.load_yaml('output/jingying/JOBTITLES', _file)
                yamldata = yamlfile['datas']
            except Exception:
                continue
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if not self.cvstorage.existscv(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info, _classify_id)
                    t1 = time.time()
                    yield job_process
                    print(time.time() - t1)
                else:
                    try:
                        yamlload = utils.builtin.load_yaml('output/jingying/RAW', cv_id+'.yaml')
                    except IOError:
                        continue
                    try:
                        yamlload.pop('tag')
                    except KeyError:
                        pass
                    yamlload['tags'] = yamldata[cv_id]['tags']
                    resultpath = self.cvstorage.addyaml(cv_id, yamlload)

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        try:
            cv_content =  self.precedure.cv(cv_info['href'])
            yamldata = self.extract_details(cv_info, cv_content)
            result = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
            job_logger.info('Download: '+cv_id)
            print('Download: '+cv_id)
        except AttributeError as e:
            job_logger.error('Downloading: '+cv_id+ ' ' + e.message)
            print('Fails Download: '+cv_id)
            self.wb_downloader.close()
            self.wb_downloader = self.get_wb_downloader(self.FF_PROFILE_PATH_BACKUPS.pop(0))
            self.precedure.wb_downloader = self.wb_downloader
            print('Switch Firefox profile!')
        result = True

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

