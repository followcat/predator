import jobs.definition.cloudshare_jingying


instance = jobs.definition.cloudshare_jingying.Jingying()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/5', hour='8-17'),
        dict(second='*/5', hour='18-23'),
        dict(second='*/5', hour='0-7')]
