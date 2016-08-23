# -*- coding: utf-8 -*-
import functools

import precedure.liepin
import jobs.classify.base
import storage.gitinterface

from sources.liepin_industry import job_list as liepin_job
from sources.industry_sources import *
from sources.industry_needed import *
from sources.industry_id import *


class Liepin(jobs.classify.base.Base):

    cookies_file = 'cookies.data'
    jobname = 'liepin'
    precedure_type = precedure.liepin.Liepin
    uldownloader=True

    def industryjob(self, industryid, filename, industry, resume=False):
        for index in industry:
            industry_id = index[0]
            industry_value = index[1]
            postinfo = {
                'industrys': industry_value
                        }
            for id_str in sorted(liepin_job.keys()):
                print postinfo['industrys'], id_str, liepin_job[id_str]['cn']
                postinfo['jobtitles'] = liepin_job[id_str]['cn']
                postdict = {
                    'industrys': industry_id,
                    'jobtitles': id_str}
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

    def jobgenerator(self, resume=False):
        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            precedure_industry = industry_dict[industry][self.jobname]
            filename = industryid
            jobs = self.industryjob(industryid, filename, precedure_industry, resume)
            for job in jobs:
                yield job


repo = storage.gitinterface.GitInterface('liepin')
instance = Liepin(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/20')]
