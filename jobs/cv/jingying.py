import jobs.definition.cloudshare_jingying


def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = jobs.definition.cloudshare_jingying.Jingying(wbdownloaders=downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC

PLAN = [dict(name='jingying_cv', second='*/10', hour='8-17'),
        dict(name='jingying_cv', second='*/60', hour='18-23'),
        dict(name='jingying_cv', second='*/60', hour='0-7')]
