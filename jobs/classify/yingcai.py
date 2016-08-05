# encoding: utf-8

import datetime
import functools

import precedure.yingcai
import storage.fsinterface
import jobs.classify.base

from sources.yingcai_source import *
from jobs.yingcai_needed import *


FF_PROFILE_PATH_LIST=['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                      '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                      '/home/winky/.mozilla/firefox/4idae7tm.winky3'
                     ]
industrys={
                '1001':"计算机／互联网／通信／电子",
                '1002':"销售／客服／技术支持",
                '1003':"会计／金融／银行／保险",
                '1004':"生产／营运采购／物流",
                '1005':"生物／制药／医疗／护理",
                '1006':"广告／市场／媒体／艺术",
                '1007':"建筑／房地产",
                '1008':"人事／行政／高级管理",
                '1009':"咨询／法律／教育／科研",
                '1010':"服务业",
                '1011':"公务员／翻译／其他"
                }
class Yingcai(jobs.classify.base.Base):

    profilepath_index=0
    FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]

    cookies_file = None
    ff_profile = FF_PROFILE_PATH

    def jobgenerator(self):
        start_time=datetime.datetime.now()
        print start_time
        yingcai=precedure.yingcai.Yingcai(wbdownloader=self.downloader)
        for industry in job_list.keys():
            #import ipdb;ipdb.set_trace()
            if len(job_list[industry].keys())==0:
                job_list[industry]=industry_list[industry]
            for job in job_list[industry].keys():
                if len(job_list[industry][job].keys())==0:
                    job_list[industry][job]=industry_list[industry][job]
                for position in job_list[industry][job].keys():
                    job_item=industry+','+job+','+position
                    postinfo={
                            'industrys': industrys[industry]
                            }
                    #postinfo['jobtitles'] = industry_list[industry][job][position]['cn']
                    print '爬取行业：{0}:{1}'.format(industry, postinfo['industrys'])
                    print '爬取职位：{0}:{1}'.format(job_item,postinfo['jobtitles'])
                    getdict = {
                            'jobType':1,
                            'live':'1,1,1',
                            'jobs':job_item,
                            'page':'0'
                            }
                    postdict = {
                            'industrys': industry,
                            'jobtitles': job_item
                            }
                    header = self.get_header(postdict, postinfo)
                    print "header:",header
                    job_process = functools.partial(yingcai.update_classify,
                                                    industry,industry,
                                                    getdict,self.repojt,header)
                    yield job_process
                    current_time = datetime.datetime.now()
                    duration=(current_time-start_time).seconds
                    if duration > 1800:
                        self.downloader.close()
                        self.profilepath_index+= 1
                        self.F_PROFILE_PATH = FF_PROFILE_PATH_LIST[self.profilepath_index%len(FF_PROFILE_PATH_LIST)]
                        self.downloader = self.get_wb_downloader(self.FF_PROFILE_PATH)
                        yingcai.wb_downloader = self.downloader
                        start_time = current_time
                    else:
                        continue

repo = storage.fsinterface.FSInterface('yingcai')
instance = Yingcai(repo)
PROCESS_GEN = instance.jobgenerator()

PLAN = [dict(second='*/5', hour='8-17'),
        dict(second='*/60', hour='18-23'),
        dict(second='*/60', hour='0-7')]
