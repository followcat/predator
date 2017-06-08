# -*- coding: utf-8 -*-
import re
import time
import logging
import functools

import utils.builtin
import precedure.zhilian
import jobs.config.zhilian
import jobs.definition.cloudshare

from sources.industry_id import *


class Zhilian(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/zhilian'
    FF_PROFILE_PATH = jobs.config.zhilian.ff_profiles[0]
    PRECEDURE_CLASS = precedure.zhilian.Zhilian
    source = 'zhilian'

    def cloudshare_yaml_template(self):
        template = super(Zhilian, self).cloudshare_yaml_template()
        template['origin'] = u'智联卓聘爬取'
        return template

    def simple_jobgenerator(self, industry_needed, keywords=None):
        for _classify_value in industry_needed:
            print(u'[zhilian cv]: 行业-%s'%_classify_value)
            _classify_id = industryID[_classify_value.encode('utf-8')]
            _file = _classify_id + '.yaml'
            try:
                yamldata = self.get_cv_list(_file, keywords)
            except IOError:
                continue
            sorted_id = sorted(yamldata, key = lambda cvid: yamldata[cvid]['date'],
                               reverse=True)
            print _file, sorted_id[0], time.localtime(yamldata[sorted_id[0]]['date'])
            for cv_id in sorted_id:
                if (time.time() - yamldata[cv_id]['date'])/60/60/24 < 14:
                    if not self.cvstorage.existscv(cv_id):
                        cv_info = yamldata[cv_id]
                        job_process = functools.partial(self.downloadjob, cv_info)
                        yield job_process
                    else:
                        cv_info = yamldata[cv_id]
                        job_process = functools.partial(self.updatejob, cv_info)
                        yield job_process

    def downloadjob(self, cv_info):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('[zhilian cv]: Download: '+cv_id)
        try:
            cv_content =  self.precedure.cv(cv_info['href'])
            if cv_content is not None:
                cvresult = True
            else:
                cvresult = False
        except precedure.zhilian.NocontentCVException:
            print('[zhilian cv]: Failed! Download: '+cv_id)
            cvresult = False
        if cvresult is True:
            yamldata = self.extract_details(cv_info, cv_content)
            cvresult = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
            job_logger.info('Download: '+cv_id)
        else:
            job_logger.info('Failed! Download: '+cv_id)
        return cvresult

    def extract_details(self, uploaded_details, cv_content):
        details = super(Zhilian, self).extract_details(uploaded_details)

        if not details['name']:
            name = uploaded_details['name']
            if len(name) == 0:
                details['name'] = uploaded_details['id']
            else:
                details['name'] = uploaded_details['name']

        if not details['age']:
            age = uploaded_details['peo'][3]
            if age:
                age_pattern = re.compile(r'(\d+)')
                details['age'] = int(re.findall(age_pattern, age)[0])
            else:
                details['age'] = ''

        if not details['education']:
            details['education'] = uploaded_details['peo'][4].replace('\n', '')\
                                   .replace('\t', '').replace('\r', '').replace(' ', '')

        if uploaded_details['info'] is not None:
            education = uploaded_details['info'][1].split('|')
            if not details['school']:
                details['school'] = education[1].replace('\n', '')\
                                    .replace('\t', '').replace('\r', '').replace(' ', '')

        if not details['tags']:
            details['tags'] = uploaded_details['tags']

        return details
