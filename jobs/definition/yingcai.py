# -*- coding: utf-8 -*-
import time
import functools

import jobs.definition.base
import storage.cv
import utils.builtin
import precedure.yingcai
import storage.fsinterface
import downloader.webdriver

class Yingcai(jobs.definition.base.Base):

    CVDB_PATH = 'output/yingcai'
    FF_PROFILE_PATH = '/home/winky/.mozilla/firefox/jvqqz5ch.winky'
    PRECEDURE_CLASS = precedure.yingcai.Yingcai

    industry_yamls = [
                      '1001', #计算机／互联网／通信／电子
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

    def __init__(self):
        self.wb_downloader = downloader.webdriver.Webdriver(self.FF_PROFILE_PATH)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.cvrepo = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.cvrepo)

    def jobgenerator(self):
        for _file in self.industry_yamls:
            yamldata = utils.builtin.load_yaml('yingcai/JOBTITLES', _file)
            if 'datas' in yamldata:
                yamldata = yamldata['datas']
            sorted_id = sorted(yamldata, key = lambda cvid: yamldata[cvid]['date'],
                               reverse=True)
            for cv_id in sorted_id:
                if (time.time() - yamldata[cv_id]['date'])/60/60/24 < 14:# not self.cvstorage.existscv(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info)
                    yield job_process
