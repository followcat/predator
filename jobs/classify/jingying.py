# -*- coding: utf-8 -*-
import functools

import precedure.jingying
import jobs.classify.base
import storage.fsinterface

from sources.jingying import *

class Jingying(jobs.classify.base.Base):

    cookies_file = 'cookies.data'
    jobname = 'jingying'
    precedure_type = precedure.jingying.Jingying
    uldownloader = True


    def industryjob(self, industryid, filename, industry, resume=False):

        for index in industry:
            add_list = []
            update_list = []
            industry_id = index[0]
            industry_value = index[1]
            print industry_value
            postdict = {'indtype': industry_id}
            postinfo = {'industry': industry_value}
            header = self.gen_header(postdict, postinfo)
            if resume and not self.eq_postdict(industryid, postdict,
                                               exclude=[self.precedure.PAGE_VAR]):
                continue
            else:
                resume = False
            job_process = functools.partial(self.precedure.update_classify,
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
        for index in industry:
            add_list = []
            update_list = []
            industry_id = index[0]
            industry_value = index[1]
            flush = False
            print industry_value
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
                    if resume and not self.eq_postdict(industryid, postdict,
                                                            exclude=[self.precedure.PAGE_VAR]):
                        continue
                    else:
                        resume = False
                    job_process = functools.partial(self.precedure.update_classify,
                                                    filename, filename,
                                                    postdict, self.repojt,
                                                    add_list, update_list,
                                                    header, flush)
                    yield job_process

repo = storage.fsinterface.FSInterface('output/jingying')
instance = Jingying(repo)
PROCESS_GEN_FUNC = instance.jobgenerator
PLAN = [dict(second='*/5')]
