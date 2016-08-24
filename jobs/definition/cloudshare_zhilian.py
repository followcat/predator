# -*- coding: utf-8 -*-
import re
import time
import logging
import functools

import utils.builtin
import precedure.zhilian
import jobs.definition.cloudshare

from sources.industry_id import *


class Zhilian(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/zhilian'
    FF_PROFILE_PATH = '/home/winky/.mozilla/firefox/jvqqz5ch.winky'
    PRECEDURE_CLASS = precedure.zhilian.Zhilian

    def cloudshare_yaml_template(self):
        template = super(Zhilian, self).cloudshare_yaml_template()
        template['origin'] = u'智联卓聘爬取'
        return template

    def jobgenerator(self, industry_needed):
        for _classify_value in industry_needed:
            _classify_id = industryID[_classify_value.encode('utf-8')]
            _file = _classify_id + '.yaml'
            try:
                yamlfile = utils.builtin.load_yaml('zhilian/JOBTITLES', _file)
                yamldata = yamlfile['datas']
            except IOError:
                continue
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info)
                    t1 = time.time()
                    yield job_process
                    print(time.time() - t1)
                else:
                    try:
                        yamlload = utils.builtin.load_yaml('output/zhilian/RAW', cv_id+'.yaml')
                    except IOError:
                        continue
                    try:
                        yamlload.pop('tag')
                    except KeyError:
                        pass
                    yamlload['tags'] = yamldata[cv_id]['tags']
                    resultpath = self.cvstorage.addyaml(cv_id, yamlload)

    def downloadjob(self, cv_info):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('Download: '+cv_id)
        try:
            cv_content =  self.precedure.cv(cv_info['href'])
            cvresult = True
        except precedure.zhilian.NocontentCVException:
            print('Failed! Download: '+cv_id)
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
            age_pattern = re.compile(r'(\d+)')
            details['age'] = int(re.findall(age_pattern, age)[0])

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
