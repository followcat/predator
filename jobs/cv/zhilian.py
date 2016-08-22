#!/usr/bin/python
# -*- coding: utf-8 -*-

import jobs.definition.cloudshare_zhilian


instance = jobs.definition.cloudshare_zhilian.Zhilian()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/6', hour='8-20'),
        dict(second='*/30', hour='21-23'),
        dict(minute='*/2', hour='0-6')]
