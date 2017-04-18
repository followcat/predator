# -*- coding: utf-8 -*-
import time
import datetime
import functools

import precedure.jingying
import jobs.classify.base
import storage.fsinterface
import jobs.config.jingying

from sources.jingying import *

class Jingying(jobs.classify.base.Base):

    source = 'jingying'
    jobname = 'jingying'
    ff_profile = jobs.config.jingying.ff_profiles[0]
    ff_profiles = jobs.config.jingying.ff_profiles
    precedure_type = precedure.jingying.Jingying
    wbdownloader = True

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


    def industryjob(self, industryid, filename, industry, keywords=None, resume=False):
        start_time=datetime.datetime.now()
        if keywords is None or len(keywords) == 0:
            keywords = ['']
        for keyword in keywords:
            for index in industry:
                add_list = []
                update_list = []
                industry_id = index[0]
                industry_value = index[1]
                print('[jingying url list]: %s' %industry_value)
                postdict = {'indtype': industry_id,
                            'fulltext':keyword.encode('gb2312')}
                postinfo = {'industry': industry_value,
                            'searchtext':keyword}
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

                for _area in self.company_area_list:
                    flush = False
                    add_list = []
                    update_list = []
                    print('[jingying url list]: %s' %_area)
                    for _index, c_name in enumerate(localdatajobs['company_name'][_area]):
                        if _index == len(localdatajobs['company_name'][_area]) - 1:
                            flush = True
                        print('[jingying url list]: %s' %c_name)
                        postdict = {'cotext': c_name.decode('utf-8').encode('gb2312'),
                                    'indtype': industry_id,
                                    'fulltext':keyword.encode('gb2312')}
                        postinfo = {'company': c_name,
                                    'industry': industry_value,
                                    'searchtext':keyword}
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
                        current_time = datetime.datetime.now()
                        duration=(current_time-start_time).seconds
                        if duration > 1800:
                            print '[jingying url list]: switch profile'
                            self.downloader.switch_profile(self.ff_profiles)
                            start_time = current_time

repo = storage.fsinterface.FSInterface('output/jingying')
PLAN = [dict(name='jingying_classify', second='*/10',hour='8-19'),
        dict(name='jingying_classify', second='*/60', hour='20-23'),
        dict(name='jingying_classify', second='*/60', hour='0-7')]

def get_PROCESS_GEN_FUNC(downloaders=None):
    instance = Jingying(repo, downloaders)
    if instance.source not in downloaders:
        downloaders[instance.source] = instance.precedure.wb_downloader
    PROCESS_GEN_FUNC = instance.jobgenerator
    return PROCESS_GEN_FUNC
