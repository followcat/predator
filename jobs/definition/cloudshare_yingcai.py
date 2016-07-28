# -*- coding: utf-8 -*-
import re
import bs4
import time
import datetime
import logging
import datetime
import functools

import utils.builtin
import precedure.yingcai
import jobs.definition.cloudshare

industry_yamls = ['1001', #计算机／互联网／通信／电子
                  '1002', #销售／客服／技术支持
                  '1003', #会计／金融／银行／保险
                  '1004', #生产／营运／采购／物流
                  '1005', #生物／制药／医疗／护理
                  '1006', #广告／市场／媒体／艺术
                  '1007', #建筑／房地产
                  '1008', #人事／行政／高级管理
                  '1009', #咨询／法律／教育／科研
                  '1010', #服务业
                  '1011', #公务员／翻译／其它
                ]

class Yingcai(jobs.definition.cloudshare.Cloudshare):

    CVDB_PATH = 'output/yingcai'
    FF_PROFILE_PATH_LIST = ['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                           '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                            '/home/winky/.mozilla/firefox/4idae7tm.winky3'
                            ]
    profilepath_index=0
    FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]
    PRECEDURE_CLASS = precedure.yingcai.Yingcai
    START_TIME=datetime.datetime.now()

    def cloudshare_yaml_template(self):
        template = super(Yingcai, self).cloudshare_yaml_template()
        template['origin'] = u'中华英才爬取'
        return template

    def jobgenerator(self):
        self.START_TIME=datetime.datetime.now()
        for _classify_id in industry_yamls:
            _file = _classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('yingcai/JOBTITLES', _file)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['info'][-1],
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
        print (cv_info['href'])
        current_time=datetime.datetime.now()
        duration=(current_time-self.START_TIME).seconds
        if duration > 1800:
            self.profilepath_index+=1
            self.FF_PROFILE_PATH=self.FF_PROFILE_PATH_LIST[self.profilepath_index]
            self.START_TIME=current_time
            cv_content =  self.precedure.cv(cv_info['href'],self.FF_PROFILE_PATH)
        else:
            cv_content =  self.precedure.cv(cv_info['href'],None)
        yamldata = self.extract_details(cv_info, cv_content)
        result = self.cvstorage.addcv(cv_id, cv_content.encode('utf-8'), yamldata)
        job_logger.info('Download: '+cv_id)
        result = True

    def extract_details(self, uploaded_details, cv_content):
        details = super(Yingcai, self).extract_details(uploaded_details)
        soup=bs4.BeautifulSoup(cv_content,'lxml')

        if not details['name']:
            name = uploaded_details['name']
            if len(name) == 0:
                details['name'] = uploaded_details['id']
            else:
                details['name'] = uploaded_details['name']

        if not details['age']:
            age = uploaded_details['info'][1]
            age_pattern = re.compile(r'(\d+)')
            details['age'] = int(re.findall(age_pattern, age)[0])

        if not details['education']:
            details['education'] = uploaded_details['info'][3].strip()
        
        return details
