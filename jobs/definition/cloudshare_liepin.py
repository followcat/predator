# -*- coding: utf-8 -*-
import logging
import functools

import pypandoc

import utils.builtin
import precedure.liepin
import jobs.definition.cloudshare

from extractor.utils_parsing import *


class Liepin(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/liepin'
    FF_PROFILE_PATH = '/home/followcat/.mozilla/firefox/yffp11op.followcat'
    PRECEDURE_CLASS = precedure.liepin.Liepin

    def cloudshare_yaml_template(self):
        template = super(Liepin, self).cloudshare_yaml_template()
        template['origin'] = u'猎聘爬取'
        return template

    def jobgenerator(self, classify_id):
        yamlname = classify_id + '.yaml'
        yamldata = utils.builtin.load_yaml('liepin/JOBTITLES', yamlname)
        sorted_id = sorted(yamldata,
                           key = lambda cvid: yamldata[cvid]['peo'][-1],
                           reverse=True)
        for cv_id in sorted_id:
            if not self.cvstorage.existscv(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.downloadjob, cv_info, classify_id)
                yield job_process

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('Download: '+cv_id)
        try:
            cv_content =  self.precedure.cv(cv_info['href'])
            cvresult = True
        except precedure.liepin.NocontentCVException:
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
        md = pypandoc.convert(cv_content, 'markdown', format='docbook')
        details = super(Liepin, self).extract_details(uploaded_details, md)
        if not details['name']:
            details['name'] = uploaded_details['name']
        if not details['age']:
            details['age']= re.compile('[0-9]*').match(uploaded_details['peo'][2]).group()
        add_cr = lambda x:'\n'+x.group()
        for education in re.compile(STUDIES, re.M).finditer(re.compile(PERIOD).sub(add_cr, uploaded_details['info'][0])):
            if not details['school']:
                details['school'] = education.group('school')
            if not details['education']:
                details['education'] = education.group('education').replace('\n', '')\
                                       .replace('\t', '').replace('\r', '').replace(' ', '')
        return details
