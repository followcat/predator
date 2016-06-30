# -*- coding: utf-8 -*-
import re
import time
import logging
import functools

import pypandoc

import jobs.definition.base
import storage.cv
import utils.builtin
import precedure.zhilian
import storage.fsinterface
import storage.jobtitles
import downloader.webdriver

from extractor.extract_experience import *
from extractor.information_explorer import *


class Zhilian(jobs.definition.base.Base):

    CVDB_PATH = 'output/zhilian'
    FF_PROFILE_PATH = '/home/kabess/.mozilla/firefox/g648khbx.default'
    PRECEDURE_CLASS = precedure.zhilian.Zhilian



    def __init__(self):
        self.wb_downloader = downloader.webdriver.Webdriver(self.FF_PROFILE_PATH)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtstorage = storage.jobtitles.JobTitles(self.fsinterface)

    def cloudshare_yaml_template(self):
        template = {
            'age': 0,
            'comment': [],
            'committer': "SCRAPPY",
            'company': "",
            'date': 0.,
            'education': "",
            'email': '',
            'experience': [],
            'filename': "",
            'id': '',
            'name': "",
            'origin': u'智联卓聘爬取',
            'phone': "",
            'position': "",
            'school': "",
            'tag': [],
            'tracking': [],
            }
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
            cvresult = self.cvstorage.add(cv_id, cv_content.encode('utf-8'))
        except precedure.zhilian.NocontentCVException:
            print('Failed! Download: '+cv_id)
            cvresult = False
        if cvresult is True:
            yamldata = self.extract_details(cv_info, cv_content)
            jtresult = self.jtstorage.add_data(cv_id, yamldata)
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
        experiences = []
        extracted_data = fix(md)
        RE = re.compile(DURATION)
        if not extracted_data[1]:
            (company, position) = extracted_data[0]
            for (i,c) in enumerate(company):
                current_positions = [p for p in position if p[4] == i]
                try:
                    if details['position'] == '':
                        details['position'] = current_positions[0][2]
                    if details['company'] == '':
                        details['company'] = company[0][2]
                except IndexError:
                    pass
                for p in current_positions:
                    if c[3] and len(current_positions) == 1 and not RE.search(p[2]):
                        experiences.append((p[0], p[1], c[2]+'|'+p[2]+'('+c[3]+')'))
                    elif c[3]:
                        experiences.append((p[0], p[1], c[2]+'('+c[3]+')'+'|'+p[2]))
                    else:
                        experiences.append((p[0], p[1], c[2]+'|'+p[2]))
                else:
                    if not len(current_positions):
                        experiences.append((c[0], c[1], c[2]))
            details['experience'] = experiences
            if u'…' in details['company']:
                details['company'] = company[0]
        return details
