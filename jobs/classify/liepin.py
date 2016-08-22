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

    def jobgenerator(self, resume=False):
        liepin = precedure.liepin.Liepin(uldownloader=self.downloader)
        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            liepin_industry = industry_dict[industry]['liepin']
            if len(liepin_industry) == 0:
                continue
            for index in liepin_industry:
                industry_id = index[0]
                industry_value = index[1]
                filename = industryid
                postinfo = {
                    'industrys': industry_value
                            }
                for id_str in liepin_job.keys():
                    print postinfo['industrys'], id_str, liepin_job[id_str]['cn']
                    postinfo['jobtitles'] = liepin_job[id_str]['cn']
                    postdict = {
                        'industrys': industry_id,
                        'jobtitles': id_str}
                    header = self.gen_header(postdict, postinfo)
                    job_process = functools.partial(liepin.update_classify,
                                                    filename, filename,
                                                    postdict, self.repojt, header)
                    yield job_process


repo = storage.gitinterface.GitInterface('liepin')
instance = Liepin(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/20')]
