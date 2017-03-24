#!/usr/bin/python
# -*- coding: utf-8 -*-

import jobs.definition.cloudshare_zhilian


def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = jobs.definition.cloudshare_zhilian.Zhilian(wbdownloaders=downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC

PLAN = [dict(name='zhilian_cv', second='*/120', hour='8-20'),
        dict(name='zhilian_cv', minute='*/5', hour='21-23'),
        dict(name='zhilian_cv', minute='*/10', hour='0-6')]
