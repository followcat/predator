import jobs.definition.cloudshare_yingcai



def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = jobs.definition.cloudshare_yingcai.Yingcai(wbdownloaders=downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC

PLAN = [dict(name='yingcai_cv', second='*/60', hour='8-19'),
        dict(name='yingcai_cv', second='*/60', hour='20-23'),
        dict(name='yingcai_cv', second='*/60', hour='0-7')]
