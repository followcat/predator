#!/usr/bin/python
# -*- coding: utf-8 -*-

import jobs.definition.cloudshare_zhilian

instance = jobs.definition.cloudshare_zhilian.Zhilian()

industry_yamls = ['160000.yaml', ##计算机/网络技术
                  '249.yaml', ##质量管理/测试经理(QA/QC经理)(质量管理/安全防护)
                  '250.yaml', ##质量管理/测试主管(QA/QC主管)(质量管理/安全防护)
                  '251.yaml', ##质量管理/测试工程师(QA/QC工程师)(质量管理/安全防护)
                  '732.yaml', ##机电工程师(工程机械)
                  '410.yaml', ##测试/可靠性工程师(电子/电气/半导体/仪器仪表)
                  '84.yaml' ##FAE现场应用工程师(电子/电气/半导体/仪器仪表)
                 ]

PROCESS_GEN = instance.jobgenerator(industry_yamls)

PLAN = [dict(second='*/6', hour='8-20'),
        dict(second='*/30', hour='21-23'),
        dict(minute='*/2', hour='0-6')]
