# -*- coding: utf-8 -*-
import functools

import precedure.zhilian
import jobs.classify.base
import storage.fsinterface

from sources.zhilian_job import *


class Zhilian(jobs.classify.base.Base):

    ff_profile = '/home/kabess/.mozilla/firefox/g648khbx.default'
    jobname = 'zhilian'
    precedure_type = precedure.zhilian.Zhilian
    wbdownloader = True

    def industryjob(self, industryid, filename, industry, resume=False):
        for index in industry:
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
                postdict = {
                    'CompanyIndustry':industry_id,
                    'JobType':job_key}
                header = self.gen_header(postdict, postinfo)
                print header
                if resume and not self.eq_postdict(industryid, postdict,
                                                   exclude=[self.precedure.PAGE_VAR]):
                    continue
                else:
                    resume = False
                job_process = functools.partial(self.precedure.update_classify,
                                                filename, filename,
                                                postdict, self.repojt, header)
                yield job_process

repo = storage.fsinterface.FSInterface('output/zhilian')

instance = Zhilian(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(minute='*/8', hour='8-20'),
        dict(minute='*/12', hour='21-23'),
        dict(minute='*/15', hour='0-6')]

