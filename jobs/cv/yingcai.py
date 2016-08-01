import jobs.definition.cloudshare_yingcai

instance = jobs.definition.cloudshare_yingcai.Yingcai()
PROCESS_GEN = instance.jobgenerator()

PLAN = [dict(second='*/60', hour='8-17'),
        dict(second='*/60', hour='18-23'),
        dict(second='*/60', hour='0-7')]
