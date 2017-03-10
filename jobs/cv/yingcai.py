import jobs.definition.cloudshare_yingcai


instance = jobs.definition.cloudshare_yingcai.Yingcai()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(name='yingcai_cv', second='*/60', hour='8-17'),
        dict(name='yingcai_cv', second='*/60', hour='18-23'),
        dict(name='yingcai_cv', second='*/60', hour='0-7')]
