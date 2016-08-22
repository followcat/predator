# encoding: utf-8

import datetime
import functools

import precedure.yingcai
import storage.fsinterface
import jobs.classify.base

from sources.yingcai import *
from sources.industry_sources import *
from sources.industry_needed import *
from sources.industry_id import *


FF_PROFILE_PATH_LIST=['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                      '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                      '/home/winky/.mozilla/firefox/4idae7tm.winky3'
                     ]

class Yingcai(jobs.classify.base.Base):

    profilepath_index=0
    FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]
    
    cookies_file = None
    ff_profile = FF_PROFILE_PATH

    def jobgenerator(self, resume=False):
        start_time=datetime.datetime.now()
        print start_time
        yingcai=precedure.yingcai.Yingcai(wbdownloader=self.downloader)
        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            yingcai_industry = industry_dict[industry]['yingcai']
            if len(yingcai_industry) == 0:
                continue
            for index in yingcai_industry:
                industry_id = index[0]
                industry_value = index[1]
                id1 = industry_id.split(',')[0]
                id2 = industry_id.split(',')[1].encode('utf-8')
                filename = industryid
                for index1 in industry_list[id1][id2].keys():
                    job_item = id1+','+id2 +','+ index1
                    postinfo = {
                                'industrys': industry_value,
                                'jobtitles': industry_list[id1][id2][index1]['cn']
                                }
                    print '爬取行业：{0}:{1}'.format(industry_id,industry_value)
                    getdict = {
                            'jobType':1,
                            'live':'1',
                            'minDegree':'4',
                            'minWorkYear':'5',
                            'jobs':job_item,
                            'page':'0'
                            }
                    postdict = {
                            'industrys': [id1,id2],
                            'job' : [id1,id2,index1] 
                            }
                    header = self.get_header(postdict, postinfo)
                    print "header:",header
                    job_process = functools.partial(yingcai.update_classify,
                                                    filename, filename,
                                                    getdict, self.repojt, header)
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

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/5', hour='8-17'),
        dict(second='*/5', hour='18-23'),
        dict(second='*/5', hour='0-7')]
