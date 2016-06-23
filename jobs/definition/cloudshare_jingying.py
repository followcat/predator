# -*- coding: utf-8 -*-
import re
import time
import logging
import datetime
import functools
import threading

import pypandoc

import jobs.definition.base
import storage.cv
import utils.builtin
import precedure.jingying
import storage.fsinterface
import downloader.webdriver

from extractor.extract_experience import *
from extractor.information_explorer import *


class Jingying(jobs.definition.base.Base):

    CVDB_PATH = 'jingying_webdrivercv'
    JT_PATH = 'additional/jingying'
    FF_PROFILE_PATH = '/home/jeff/.mozilla/firefox/ozyc3tvj.jeff'
    PRECEDURE_CLASS = precedure.jingying.Jingying

    industry_yamls = ['47', #医疗设备/器械
                      '01', #计算机软件
                      '37', #计算机硬件
                      '38', #计算机服务(系统、数据服务、维修)
                      '31', #通信/电信/网络设备
                      '35', #仪器仪表/工业自动化
                      '14', #机械/设备/重工
                      '52', #检测，认证
                      '07', #专业服务(咨询、人力资源、财会)
                      '24', #学术/科研
                      '21', #交通/运输/物流
                      '55', #航天/航空
                      '36', #电气/电力/水利
                      '61'  #新能源
                    ]

    def __init__(self):
        self.wb_downloader = downloader.webdriver.Webdriver(self.FF_PROFILE_PATH)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.cvrepo = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.cvrepo)
        self.fsinterface = storage.fsinterface.FSInterface(self.JT_PATH)
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
            'origin': u'无忧精英爬取',
            'phone': "",
            'position': "",
            'school': "",
            'tag': [],
            'tracking': [],
            }
        return template

    def jobgenerator(self):
        for _classify_id in self.industry_yamls:
            _file = _classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', _file)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info, _classify_id)
                    t1 = time.time()
                    yield job_process
                    print(time.time() - t1)

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('Download: '+cv_id)
        cv_content =  self.precedure.cv(cv_info['href'])
        result = self.cvstorage.add(cv_id, cv_content.encode('utf-8'), 'followcat')
        yamldata = self.extract_details(cv_info, cv_content)
        jtresult = self.jtstorage.add_datas(classify_id, [yamldata], 'followcat')
        job_logger.info('Download: '+cv_id)
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
        details = self.cloudshare_yaml_template()
        md = pypandoc.convert(cv_content, 'markdown', format='docbook')
        details['date'] = time.time()
        details['id'] = uploaded_details['id']
        details['filename'] = uploaded_details['href']
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

        re_born_date = u'(\d{4})年(\d{1,2})月(\d{1,2})日'
        res = get_infofromrestr(md.encode('utf-8'), re_born_date)

        if details['company'] == '':
            details['company'] = uploaded_details['peo'][2]
        if details['position'] == '':
            details['position'] = uploaded_details['peo'][0]
        if len(res) > 0 and len(res[0]) == 3:
            age_res = res[0]
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
            details['age'] = age
        details['education'] = get_tagfromstring('学历', md.encode('utf-8'))
        details['school'] = get_tagfromstring('学校', md.encode('utf-8'))

        return details

