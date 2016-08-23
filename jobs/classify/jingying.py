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

    def jobgenerator(self, resume=False):
        jingying = precedure.jingying.Jingying(uldownloader=self.downloader)

        for _index, industry in enumerate(industry_needed):
            industry = industry.encode('utf-8')
            industryid = industryID[industry]
            filename = industryid
            jingying_industry = industry_dict[industry]['jingying']
            temp_resume = resume
            for index in jingying_industry:
                add_list = []
                update_list = []
                industry_id = index[0]
                industry_value = index[1]
                print industry, industry_value
                postdict = {'indtype': industry_id}
                postinfo = {'industry': industry_value}
                header = self.gen_header(postdict, postinfo)
                if temp_resume and not self.eq_postdict(industryid, postdict,
                                                exclude=[jingying.PAGE_VAR]):
                    continue
                else:
                    temp_resume = False
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
            for index in jingying_industry:
                add_list = []
                update_list = []
                industry_id = index[0]
                industry_value = index[1]
                flush = False
                print industry, industry_value
                for _index, _area in enumerate(company_area_list):
                    print _area
                    if _index == len(company_area_list) - 1:
                        flush = True
                    for c_name in localdatajobs['company_name'][_area]:
                        print c_name
                        postdict = {'cotext': c_name.decode('utf-8').encode('gb2312'),
                                    'indtype': industry_id}
                        postinfo = {'company': c_name,
                                    'industry': industry_value}
                        header = self.gen_header(postdict, postinfo)
                        if temp_resume and not self.eq_postdict(industryid, postdict,
                                                                exclude=[jingying.PAGE_VAR]):
                            continue
                        else:
                            temp_resume = False
                        job_process = functools.partial(jingying.update_classify,
                                                        filename, filename,
                                                        postdict, self.repojt,
                                                        add_list, update_list,
                                                        header, flush)
                        yield job_process

repo = storage.fsinterface.FSInterface('jingying')
instance = Jingying(repo)
PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/5')]
