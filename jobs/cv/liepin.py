import jobs.definition.cloudshare_liepin


instance = jobs.definition.cloudshare_liepin.Liepin()

PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(minute='*/5', hour='8-17'),
        dict(minute='*/15', hour='18-23'),
        dict(minute='*/15', hour='0-2')]
