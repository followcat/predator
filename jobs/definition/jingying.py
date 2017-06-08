# -*- coding: utf-8 -*-
import time
import functools

import jobs.definition.base
import storage.cv
import utils.builtin
import precedure.jingying
import storage.fsinterface
import downloader.webdriver



class Jingying(jobs.definition.base.Base):

    CVDB_PATH = 'jingying_webdrivercv'
    FF_PROFILE_PATH = '/home/jeff/.mozilla/firefox/16xuwjcx.51jingying_2'
    PRECEDURE_CLASS = precedure.jingying.Jingying

    industry_yamls = ['47.yaml', #医疗设备/器械
                      '01.yaml', #计算机软件
                      '37.yaml', #计算机硬件
                      '38.yaml', #计算机服务(系统、数据服务、维修)
                      '31.yaml', #通信/电信/网络设备
                      '35.yaml', #仪器仪表/工业自动化
                      '14.yaml', #机械/设备/重工
                      '52.yaml', #检测，认证
                      '07.yaml', #专业服务(咨询、人力资源、财会)
                      '24.yaml', #学术/科研
                      '21.yaml', #交通/运输/物流
                      '55.yaml', #航天/航空
                      '36.yaml', #电气/电力/水利
                      '61.yaml'  #新能源
                    ]

    def __init__(self):
        self.wb_downloader = downloader.webdriver.Webdriver(self.FF_PROFILE_PATH)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.cvrepo = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.cvrepo)

    def jobgenerator(self):
        for _file in self.industry_yamls:
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', _file)
            if 'datas' in yamldata:
                yamldata = yamldata['datas']
            sorted_id = sorted(yamldata, key = lambda cvid: yamldata[cvid]['date'],
                               reverse=True)
            for cv_id in sorted_id:
                if not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info)
                    t1 = time.time()
                    yield job_process
                    print(time.time() - t1)
