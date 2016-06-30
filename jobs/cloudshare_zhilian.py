# -*- coding: utf-8 -*-
import time
import logging
import functools
import bs4
import jobs.base
import utils.builtin
import precedure.zhilian
import storage.cv
import storage.jobtitles
import storage.fsinterface
import downloader.webdriver

from extractor.utils_parsing import *


class Zhilian(object):

    CVDB_PATH = 'zhilian_cv'
    JT_PATH = 'additional/zhilian'
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
            'origin': u'智联爬取',
            'phone': "",
            'position': "",
            'school': "",
            'tag': [],
            'tracking': [],
            }
        return template

    def jobgenerator(self, classify_id):
        yamlname = classify_id + '.yaml'
        yamldata = utils.builtin.load_yaml('zhilian/JOBTITLES', yamlname)
        sorted_id = sorted(yamldata,
                           key = lambda cvid: yamldata[cvid]['peo'][-1],
                           reverse=True)
        for cv_id in sorted_id:
            if not self.cvstorage.exists(cv_id):
                cv_info = yamldata[cv_id]
                job_process = functools.partial(self.downloadjob, cv_info, classify_id)
                yield job_process

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('Download: '+cv_id)
        cv_content =  self.precedure.cv(cv_info['href'])
        cvresult = self.cvstorage.add(cv_id, cv_content.encode('utf-8'))
        yamldata = self.extract_details(cv_info)
        jtresult = self.jtstorage.add_datas(classify_id, [yamldata])
        job_logger.info('Download: '+cv_id)
        result = True

    def extract_details(self, uploaded_details):
        details = self.cloudshare_yaml_template()

        details['date'] = time.time()
        details['name'] = uploaded_details['name']
        details['id'] = uploaded_details['id']
        details['age'] = uploaded_details['peo'][3]
        details['company'] = uploaded_details['peo'][1]
        details['position'] = uploaded_details['peo'][0]
        details['education'] = uploaded_details['peo'][4]
        details['filename'] = uploaded_details['href']
        if uploaded_details['info'] is not None:
            education = uploaded_details['info'][1].split('|')
            details['education_time'] = education[0]
            details['school'] = education[1]
            details['major'] = education[2]
            expe = uploaded_details['info'][2].split('|')
            details['experience'] = []
            details['experience'].append((expe[0].split('-')[0], expe[0].split('-')[1], expe[1], expe[2]))

        if u'…' in details['company']:
            htmlsource = details['html']
            bs = bs4.BeautifulSoup(htmlsource, 'lxml')
            details['company'] = bs.find(class_='hl').get('title')
        return details

instance = Zhilian()

PROCESS_GEN = instance.jobgenerator('160000')
PLAN = [dict(second='*/5', hour='8-19'),
        dict(minute='*/2', hour='20-23'),
        dict(minute='*/5', hour='0-2')]
