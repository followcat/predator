# -*- coding: utf-8 -*-
import functools

import precedure.liepin
import jobs.classify.base
import jobs.config.liepin
import storage.fsinterface

from sources.liepin_industry import job_list as liepin_job


class Liepin(jobs.classify.base.Base):

    ff_profile = jobs.config.liepin.ff_profiles[0]
    jobname = 'liepin'
    source = 'liepin'
    precedure_type = precedure.liepin.Liepin
    wbdownloader = True

    def industryjob(self, industryid, filename, industry, keywords=None, resume=False):
        if keywords is None or len(keywords) == 0:
            keywords = ['']
        for keyword in keywords:
            for index in industry:
                industry_id = index[0]
                industry_value = index[1]
                postinfo = {
                    'industrys': industry_value,
                    'searchtext': keyword,
                            }
                for id_str in sorted(liepin_job.keys()):
                    postdict = {
                        'industrys': industry_id,
                        'keys': keyword.encode('utf-8'),
                        }
                    if keyword != '':
                        print postinfo['industrys'], keyword
                    else:
                        print postinfo['industrys'], id_str, liepin_job[id_str]['cn']
                        postinfo['jobtitles'] = liepin_job[id_str]['cn']
                        postdict['jobtitles'] = id_str
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
                    if  keyword != '':
                        break


repo = storage.fsinterface.FSInterface('output/liepin')
instance = Liepin(repo)

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/120')]
