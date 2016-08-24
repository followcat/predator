# encoding: utf-8

import datetime
import functools

import precedure.yingcai
import storage.fsinterface
import jobs.classify.base

from sources.yingcai_job import *


FF_PROFILE_PATH_LIST=['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                      '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                      '/home/winky/.mozilla/firefox/4idae7tm.winky3'
                     ]

class Yingcai(jobs.classify.base.Base):

    profilepath_index=0
    FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]
    
    cookies_file = None
    ff_profile = FF_PROFILE_PATH

    jobname = 'yingcai'
    precedure_type = precedure.yingcai.Yingcai
    wbdownloader = True

    def industryjob(self, industryid, filename, industry, resume=False):
        start_time=datetime.datetime.now()
        print start_time
        for index in industry:
            industry_id = index[0]
            industry_value = index[1]
            for index1 in sorted(job_list.keys()):
                job_item = index1
                postinfo = {
                            'industrys': industry_value,
                            'jobtitles': job_list[index1]
                            }
                print '爬取行业：{0}:{1}'.format(industry_id, industry_value)
                getdict = {
                        'jobs':job_item,
                        'wishIndustry':industry_id,
                        'page':'0'
                        }
                header = self.gen_header(getdict, postinfo)
                #import ipdb;ipdb.set_trace()
                print "header:",header
                if resume and not self.eq_postdict(industryid, getdict,
                                                   exclude=[self.precedure.PAGE_VAR]):
                    continue
                else:
                    resume = False
                job_process = functools.partial(self.precedure.update_classify,
                                                filename, filename,
                                                getdict, self.repojt, header)
                yield job_process
                current_time = datetime.datetime.now()
                duration=(current_time-start_time).seconds
                if duration > 1800:
                    self.downloader.close()
                    self.profilepath_index += 1
                    self.F_PROFILE_PATH = FF_PROFILE_PATH_LIST[self.profilepath_index%len(FF_PROFILE_PATH_LIST)]
                    self.downloader = self.get_wb_downloader(self.FF_PROFILE_PATH)
                    self.precedure.wb_downloader = self.downloader
                    start_time = current_time
                else:
                    continue

repo = storage.fsinterface.FSInterface('yingcai')
instance = Yingcai(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/5', hour='8-17'),
        dict(second='*/5', hour='18-23'),
        dict(second='*/5', hour='0-7')]
