# -*- coding: utf-8 -*-

import time
import urllib

import bs4

import utils.tools
import precedure.base

class NocontentCVException(Exception):
    pass

class Zhilian(precedure.base.Base):

    BASE_URL='http://h.highpin.cn'
    PAGE_VAR = 'PageIndex'
    CLASSIFY_SLEEP = 5
    CLASSIFY_MAXPAGE = 100

    urls_data = {
        'Q':'',
        'IsJobTitleOnly':'false',
        'IsPartialMatch':'false',
        'CompanyName':'',
        'IsArecent':'false',
        'DesiredWorkLocation':'',
        'JobLocation':'',
        'AdegreeMin':2,
        'AdegreeMax':9,
        'WorkExperienceMin':-1,
        'WorkExperienceMax':-1,
        'AgeMin':'',
        'AgeMax':'',
        'Gender':-1,
        'Language':-1,
        'Language1':-1,
        'Ability1':-1,
        'Language2':-1,
        'Ability2':-1,
        'Language3':-1,
        'Ability3':-1,
        'OverseasJobExperience':-1,
        'WorkStatus':-1,
        'SchoolName':'',
        'ProfessionalTitle':'',
        'PageSize':30,
        'Sort':'scoe desc',
        'IsAbstract':'true',
    }

    def __init__(self, url_downloader=None, wbdownloader=None):
        self.url_downloader = url_downloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_data = dict()
        tmp_data.update(self.urls_data)
        tmp_data.update(data)
        searchurl = 'http://h.highpin.cn/SearchResume/SearchResumeList?'
        params_str = urllib.urlencode(tmp_data)
        download_url = searchurl + params_str
        print 'download url: ' + download_url
        return self.wb_downloader.getsource(download_url)

    def urlget_cv(self, url):
        download_url = 'http://h.highpin.cn' + url
        print 'download url: ' + download_url
        return self.url_downloader.get(download_url)

    def parse_classify(self, htmlsource, header):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        data_lists = bs.findAll(class_='bor-bottom')

        no_search_box = bs.findAll(class_='h-no-search-box')
        error_box = bs.findAll(class_='box-404')
        if len(no_search_box) > 0 or len(error_box) > 0:
            return None

        result = []
        for index in range(1, len(data_lists), 2):
            storage_data = { 'peo': [], 'info': [] }
            storage_data['date'] = time.time()
            storage_data['recommend'] = ''
            storage_data['elite'] = ''
            storage_data['name'] = ''
            storage_data['data-name'] = ''
            storage_data['data-id'] = ''
            cur_situation = data_lists[index]
            abstract = data_lists[int(index+1)]
            storage_data['html'] = cur_situation.prettify() + abstract.prettify()
            peo_list = cur_situation.findAll(class_='list-three')
            for peo_item in peo_list:
                if peo_item.find("a") is not None:
                    element_a = peo_item.find("a")
                    storage_data['href'] = element_a.get('href')
                    query_str = utils.tools.queryString(element_a.get('href'))
                    storage_data['id'] = query_str['resumeID']
                    storage_data['data-userid'] = query_str['seekerUserID']
                    storage_data['title'] = peo_item.get('title')
                    storage_data['peo'].append(peo_item.get('title'))
                else:
                    storage_data['peo'].append(peo_item.text)
            info_list = abstract.find_all("p")
            for info_item in info_list:
                storage_data['info'].append(info_item.text)
            storage_data['tags'] = {}
            for index in header['tags'].keys():
                storage_data['tags'][index] = set()
                storage_data['tags'][index].add(header['tags'][index])
            result.append(storage_data)
        return result

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        recommand = bs.find(id='recommand-btn-area')
        recommand.decompose()
        send_contact = bs.find(id='haveSeenContact')
        send_contact.decompose()
        contact_type = bs.find(id='showContactType')
        contact_type.decompose()
        label = bs.find(class_='evalListsInnerBox')
        if label is not None:
            label_link = label.findAll('a')
            for e in label_link:
                e.decompose()
        detail_content = bs.find(class_='detail-con')
        resume_content = bs.find(class_='detail-tabs-new')
        return detail_content.prettify() + resume_content.prettify()

    def classify(self, params_data, header):
        htmlsource = self.urlget_classify(params_data)
        result = self.parse_classify(htmlsource, header)
        # if len(result) == 0:
        #     if u'抱歉没有找到当前搜索条件的相关结果' in htmlsource:
        #         result = None
        #     else:
        #         self.logException(htmlsource)
        return result
