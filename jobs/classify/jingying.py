# -*- coding: utf-8 -*-
import functools

import precedure.jingying
import jobs.classify.base
import storage.fsinterface

from sources.jingying import *

from sources.industry_sources import *
from sources.industry_needed import *
from sources.industry_id import *

class Jingying(jobs.classify.base.Base):

    cookies_file = 'cookies.data'

    def jobgenerator(self):
        jingying = precedure.jingying.Jingying(uldownloader=self.downloader)

        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            filename = industryid
            jingying_industry = industry_dict[industry]['jingying']
            add_list = []
            update_list = []
            if len(jingying_industry) == 0:
                continue
            for index in jingying_industry:
                industry_id = index[0]
                industry_value = index[1]
                print industry_value
                postdict = {'indtype': industry_id}
                postinfo = {'industry': industry_value}
                header = self.get_header(postdict, postinfo)
                job_process = functools.partial(jingying.update_classify,
                                                filename, filename,
                                                postdict, self.repojt,
                                                add_list, update_list,
                                                header)
                yield job_process

        company_area_list = [
            'GuangDong',        #广东
            'ShangHai',         #上海
            'JiangSu',          #江苏
            'BeiJing',          #北京
            'ZheJiang',         #浙江
            'HuNan',            #湖南
            'AnHui',            #安徽
            'JiangXi',          #江西
            'GuangXi',          #广西
            'SiChuan',          #四川
            'NorthEast',        #东北
            'ShanDong',         #山东
            'TianJin',          #天津
            'ShanXi(Shan)',     #陕西（陕）
            'ShanXi(Jin)',      #山西（晋）
            'HeBei',            #河北
            'HuBei',            #湖北
            'FuJian',           #福建
            'Others',           #其他
            ]
        for industry in industry_needed:
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            filename = industryid
            jingying_industry = industry_dict[industry]['jingying']
            add_list = []
            update_list = []
            for index in jingying_industry:
                industry_id = index[0]
                industry_value = index[1]
                flush = False
                for _index, _area in enumerate(company_area_list):
                    if _index == len(company_area_list) - 1:
                        flush = True
                    for c_name in localdatajobs['company_name'][_area]:
                        print c_name
                        postdict = {'cotext': c_name.decode('utf-8').encode('gb2312'),
                                    'indtype': industry_id}
                        postinfo = {'company': c_name,
                                    'industry': industry_value}
                        header = self.get_header(postdict, postinfo)
                        job_process = functools.partial(jingying.update_classify,
                                                        filename, filename,
                                                        postdict, self.repojt,
                                                        add_list, update_list,
                                                        header, flush)
                        yield job_process

repo = storage.fsinterface.FSInterface('jingying')
instance = Jingying(repo)
PROCESS_GEN = instance.jobgenerator()
PLAN = [dict(second='*/5')]
