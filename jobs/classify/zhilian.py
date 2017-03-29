# -*- coding: utf-8 -*-
import functools

import precedure.zhilian
import jobs.classify.base
import jobs.config.zhilian
import storage.fsinterface

from sources.zhilian_job import *


class Zhilian(jobs.classify.base.Base):

    ff_profile = jobs.config.zhilian.ff_profiles[0]
    jobname = 'zhilian'
    source = 'zhilian'
    precedure_type = precedure.zhilian.Zhilian
    wbdownloader = True

    def industryjob(self, industryid, filename, industry, keywords=None, resume=False):
        if keywords is None or len(keywords) == 0:
            keywords = ['']
        for keyword in keywords:
            for index in industry:
                industry_id = index[0]
                industry_value = index[1]
                print '[zhilian url list]: 抓取的行业：' + industry_value
                postinfo = {
                    'industrys': industry_value,
                    'searchtext': keyword,
                        }
                for job_key in sorted(jobtype_list.keys()):
                    job_type = jobtype_list[job_key].encode('utf-8')
                    print "[zhilian url list]: 正在抓取的职位: " + job_type
                    postinfo['jobtitles'] = job_type
                    postdict = {
                        'Q': keyword.encode('utf-8'),
                        'CompanyIndustry': industry_id,
                        'JobType': job_key}
                    header = self.gen_header(postdict, postinfo)
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

PLAN = [dict(name='zhilian_classify', minute='*/2', hour='8-20'),
        dict(name='zhilian_classify', minute='*/12', hour='21-23'),
        dict(name='zhilian_classify', minute='*/15', hour='0-6')]

def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = Zhilian(repo, downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC
