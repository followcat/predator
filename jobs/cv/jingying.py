import jobs.definition.cloudshare_jingying


instance = jobs.definition.cloudshare_jingying.Jingying()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(name='jingying_cv', second='*/10', hour='8-17'),
        dict(name='jingying_cv', second='*/60', hour='18-23'),
        dict(name='jingying_cv', second='*/60', hour='0-7')]
