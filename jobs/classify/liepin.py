# -*- coding: utf-8 -*-
import functools

import precedure.liepin
import jobs.classify.base
import storage.gitinterface


class Liepin(jobs.classify.base.Base):

    cookies_file = 'cookies.data'

    def jobgenerator(self):
        liepin = precedure.liepin.Liepin(uldownloader=self.downloader)
        industrys = {
            290: u'生物/制药/医疗器械'
        }
        selected_list = {
            '290094': u'医疗器械研发',
            '290097': u'医疗器械生产/质量管理',
            '060010': u'市场总监',
            '020010': u'销售总监',
            '040020': u'项目经理/主管',
            '040040': u'项目专员/助理',
            '050010': u'质量管理/测试经理(QA/QC经理)',
            '050080': u'体系工程师/审核员',
            '050020': u'质量管理/测试主管(QA/QC主管)',
        }
        for indu in industrys:
            postinfo = {
                'industrys': industrys[indu]
            }
            for id_str in selected_list:
                print postinfo['industrys'], selected_list[id_str], id_str
                postinfo['jobtitles'] = selected_list[id_str]
                postdict = {
                    'industrys': indu,
                    'jobtitles': id_str,
                    'curPage': 0}
                header = self.get_header(postdict, postinfo)
                job_process = functools.partial(liepin.update_classify,
                                                postdict, self.repojt, header)
                yield job_process


repo = storage.gitinterface.GitInterface('liepin')
instance = Liepin(repo)
PROCESS_GEN = instance.jobgenerator()
PLAN = [dict(minute='*/5')]
