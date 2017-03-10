#!/usr/bin/python
# -*- coding: utf-8 -*-

import jobs.definition.cloudshare_zhilian


instance = jobs.definition.cloudshare_zhilian.Zhilian()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(name='zhilian_cv', second='*/120', hour='8-20'),
        dict(name='zhilian_cv', minute='*/5', hour='21-23'),
        dict(name='zhilian_cv', minute='*/10', hour='0-6')]
