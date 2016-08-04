# -*- coding: utf-8 -*-

import time

import bs4
import json

import utils.tools
import precedure.base


class Jingying(precedure.base.Base):

    BASE_URL='http://www.51jingying.com'
    PAGE_VAR = 'curr_page'
    CLASSIFY_SLEEP = 10
    CLASSIFY_MAXPAGE = 20

    post_data = {
        'url': '/spy/searchmanager.php?act=getSpySearch',
        'nisseniordb': 1, #0-高级人才库, 1-全部人才库, 2-御用精英人才库
        'indtype': '',
        'potext': '',
        'cotext': '',
        'fulltext': '',
        'div': '',
        'niscohis': 1,
        'jobarea': '',
        'isexarea': 0,
        'curcompany': '',
        'poslevel': '',
        'cotype': '',
        'cosize': '',
        'degree': '',
        'gender': '',
        'isexsalary': 0,
        'startsalary': '',
        'endsalary': '',
        'startage': '',
        'endage': '',
        'startworkyear': '',
        'endworkyear': '',
        'HisCompany': '',
        'corepos': '',
        'pre_page': 1,
        'result':[],
        'totalcount': 0,
        'type': 'searchall'}

    def __init__(self, uldownloader=None, wbdownloader=None):
        self.ul_downloader = uldownloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_post = dict()
        tmp_post.update(self.post_data)
        tmp_post.update(data)
        searchurl = 'http://www.51jingying.com/spy/searchmanager.php?act=getSpySearch'
        return self.ul_downloader.post(searchurl, data=tmp_post)

    def urlget_cv(self, url):
        download_url = BASE_URL + url
        return self.ul_downloader.get(download_url)

    def parse_classify(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, "lxml")
        items = bs.findAll(class_='f-information-list border mb-15')
        results = []
        for index in range(len(items)):
            storage_data = {'peo':[], 'info':[]}
            index_bs = items[index]
            storage_data['html'] = index_bs.prettify()
            storage_data['id'] = str(index_bs['objectoriginalid'])
            storage_data['data-name'] = ''
            storage_data['date'] = time.time()
            storage_data['data-userid'] = ''
            storage_data['recommend'] = ''
            _elite = index_bs.find(class_='yu pos-l-22')
            storage_data['elite'] = _elite is not None
            blank = index_bs.find(target='_blank')
            storage_data['href'] = blank['href']
            storage_data['name'] = ''
            storage_data['title'] = ''
            storage_data['data-id'] = ''
            for td in index_bs.findAll('span', class_="mr-20"):
                info = None
                parent = td.findParent()
                if parent.name == 'a':
                    info = utils.tools.replace_tnr(td.text)
                if td.has_attr('title'):
                    info = utils.tools.replace_tnr(td['title'])
                if info is not None:
                    storage_data['peo'].append(info)
            date_span = index_bs.find('span', class_='f-12 f-day')
            storage_data['peo'].append(date_span.text)
            text_info = index_bs.find(class_="f-information-box")
            storage_data['info'].append(text_info.text)
            results.append(storage_data)
        return results

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        content = bs.find(id='51jobcv')
        if content is None:
            content = bs.find(id='profile')
        style = content.find('style')
        if style is not None:
            style.decompose()
        meta = content.find('meta')
        if meta is not None:
            meta.decompose()
        return content.prettify()

    def classify(self, postdata):
        json_res = self.urlget_classify(postdata)
        try:
            htmlsource = json.loads(json_res)['html']
        except KeyError:
            pass
        result = self.parse_classify(htmlsource)
        return result
