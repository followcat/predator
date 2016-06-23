#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools
import utils.builtin
import precedure.zhilian
import jobs.definition.base

class Zhilian(jobs.definition.base.Base):
    CVDB_PATH = 'zhilian_cv'
    FF_PROFILE_PATH = '/home/kabess/.mozilla/firefox/g648khbx.default'
    PRECEDURE_CLASS = precedure.zhilian.Zhilian

    industry_yamls = ['160000.yaml', ##计算机/网络技术
                      '249.yaml', ##质量管理/测试经理(QA/QC经理)(质量管理/安全防护)
                      '250.yaml', ##质量管理/测试主管(QA/QC主管)(质量管理/安全防护)
                      '251.yaml', ##质量管理/测试工程师(QA/QC工程师)(质量管理/安全防护)
                      '732.yaml', ##机电工程师(工程机械)
                      '410.yaml', ##测试/可靠性工程师(电子/电气/半导体/仪器仪表)
                      '84.yaml' ##FAE现场应用工程师(电子/电气/半导体/仪器仪表)
                     ]

    def jobgenerator(self):
        for _file in self.industry_yamls:
            yamldata = utils.builtin.load_yaml('zhilian/JOBTITLES', _file)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse = True)
            for cv_id in sorted_id:
                if not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.downloadjob, cv_info)
                    yield job_process


instance = Zhilian()
PROCESS_GEN = instance.jobgenerator()

PLAN = [dict(second='*/10', hour='8-20'),
        dict(minute='*/5', hour='21-23'),
        dict(minute='*/10', hour='0-2')]
