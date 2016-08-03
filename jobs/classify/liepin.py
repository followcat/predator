import functools

import precedure.liepin
import jobs.classify.base
import storage.gitinterface

from sources.liepin import localdatajobs


class Liepin(jobs.classify.base.Base):

    cookies_file = 'cookies.data'

    def jobgenerator(self):
        liepin = precedure.liepin.Liepin(uldownloader=self.downloader)
        selected_list = [
        '290094', #医疗器械研发
        '290097', #医疗器械生产/质量管理
        '060010', #市场总监
        '020010', #销售总监
        '040020', #项目经理/主管
        '040040', #项目专员/助理
        '050010', #质量管理/测试经理(QA/QC经理)
        '050080', #体系工程师/审核员
        '050020', #质量管理/测试主管(QA/QC主管)
        ]
        for id_str in selected_list:
            print localdatajobs['jobtitles'][id_str][0]
            postdict = {'industrys': 290,
                        'jobtitles': id_str,
                        'curPage': 0}
            job_process = functools.partial(liepin.update_classify, postdict, self.repojt)
            yield job_process


repo = storage.gitinterface.GitInterface('liepin')
instance = Liepin(repo)
PROCESS_GEN = instance.jobgenerator()
PLAN = [dict(minute='*/5')]
