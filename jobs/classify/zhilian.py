# -*- coding: utf-8 -*-
import functools

import precedure.zhilian
import jobs.classify.base
import storage.gitinterface

from sources.industry_sources import *
from sources.industry_needed import *
from sources.industry_id import *
from sources.zhilian_job import *

class Zhilian(jobs.classify.base.Base):

    ff_profile = '/home/winky/.mozilla/firefox/rikqqhcg.default'

    def jobgenerator(self, resume=False):
        
        zhilian = precedure.zhilian.Zhilian(wbdownloader = self.downloader)

        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            zhilian_industry = industry_dict[industry]['zhilian']
            filename = industryid
            temp_resume = resume
            for index in zhilian_industry:
                industry_id = index[0]
                industry_value = index[1]
                print '抓取的行业：' + industry_value
                postinfo = {
                    'industrys': industry_value
                            }
                for job_key in sorted(jobtype_list.keys()):
                    job_type = jobtype_list[job_key].encode('utf-8')
                    print "正在抓取的职位: " + job_type
                    postinfo['jobtitles'] = job_type
                    paramsdict = {
                            'CompanyIndustry':industry_id,
                            'JobType':job_key
                        }
                    header = self.gen_header(paramsdict, postinfo)
                    print header
                    if temp_resume and not self.eq_postdict(industryid, paramsdict):
                        continue
                    else:
                        temp_resume = False
                    job_process = functools.partial(zhilian.update_classify,
                                                filename, filename,
                                                 paramsdict, self.repojt, header)
                    yield job_process

repo = storage.gitinterface.GitInterface('zhilian')
instance = Zhilian(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/6', hour='8-20'),
        dict(second='*/30', hour='21-23'),
        dict(minute='*/2', hour='0-6')]

