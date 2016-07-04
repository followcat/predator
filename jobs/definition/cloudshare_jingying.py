# -*- coding: utf-8 -*-
import time
import logging
import datetime
import functools

import utils.builtin
import precedure.jingying
import jobs.definition.cloudshare


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

class Jingying(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'jingying_webdrivercv'
    FF_PROFILE_PATH = '/home/jeff/.mozilla/firefox/ozyc3tvj.jeff'
    PRECEDURE_CLASS = precedure.jingying.Jingying

    def cloudshare_yaml_template(self):
        template = super(Jingying, self).cloudshare_yaml_template()
        template['origin'] = u'无忧精英爬取'
        return template

    def jobgenerator(self):
        for _classify_id in industry_yamls:
            _file = _classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', _file)
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

    def downloadjob(self, cv_info, classify_id):
        job_logger = logging.getLogger('schedJob')
        cv_id = cv_info['id']
        print('Download: '+cv_id)
        cv_content =  self.precedure.cv(cv_info['href'])
        yamldata = self.extract_details(cv_info, cv_content)
        result = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
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
        details = super(Jingying, self).extract_details(uploaded_details)

        if not details['age']:
            re_born_date = u'(\d{4})年(\d{1,2})月(\d{1,2})日'
            res = get_infofromrestr(cv_content, re_born_date)
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

        return details

