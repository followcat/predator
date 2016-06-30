# -*- coding: utf-8 -*-
import re
import time
import logging
import functools

import pypandoc

import utils.builtin
import precedure.zhilian
import jobs.definition.cloudshare

from extractor.extract_experience import *
from extractor.information_explorer import *


class Zhilian(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/zhilian'
    FF_PROFILE_PATH = '/home/kabess/.mozilla/firefox/g648khbx.default'
    PRECEDURE_CLASS = precedure.zhilian.Zhilian

    def cloudshare_yaml_template(self):
        template = super(Zhilian, self).cloudshare_yaml_template()
        template['origin'] = u'智联卓聘爬取'
        return template

    def jobgenerator(self, industry_yamls):
        for _file in industry_yamls:
            #_file = _classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('zhilian/JOBTITLES', _file)
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
        details = self.cloudshare_yaml_template()

        details['date'] = time.time()
        name = uploaded_details['name']
        if len(name) == 0:
            details['name'] = uploaded_details['id']
        else:
            details['name'] = uploaded_details['name']
        details['id'] = uploaded_details['id']
        age = uploaded_details['peo'][3]
        age_pattern = re.compile(r'(\d+)')
        details['age'] = re.findall(age_pattern, age)[0]

        details['education'] = uploaded_details['peo'][4]
        details['filename'] = uploaded_details['href']
        if uploaded_details['info'] is not None:
            education = uploaded_details['info'][1].split('|')
            details['school'] = education[1]
            details['major'] = education[2]

        md = pypandoc.convert(cv_content, 'markdown', format='docbook')
        details.update(get_experience(md))
        return details