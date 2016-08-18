# -*- coding: utf-8 -*-

import time

import bs4

import utils.tools
import precedure.base


class NocontentCVException(Exception):
    pass

class Liepin(precedure.base.Base):

    BASE_URL='https://h.liepin.com'
    PAGE_VAR = 'curPage'
    CLASSIFY_SLEEP = 10
    CLASSIFY_MAXPAGE = 100

    urls_post = {
        'form_submit':1,
        'keys':'',
        'titleKeys':'',
        'company':'',
        'company_type':0,
        'industrys':'',
        'jobtitles':'',
        'dqs':'',
        'wantdqs':'',
        'workyearslow':'',
        'workyearshigh':'',
        'edulevellow':'',
        'edulevelhigh':'',
        'agelow':'',
        'agehigh':'',
        'sex':'',
        'pageSize':50}

    def __init__(self, uldownloader=None, wbdownloader=None):
        self.ul_downloader = uldownloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_post = dict()
        tmp_post.update(self.urls_post)
        tmp_post.update(data)
        searchurl = 'https://h.liepin.com/cvsearch/soResume/'
        return self.ul_downloader.post(searchurl, data=tmp_post)

    def urlget_cv(self, url):
        download_url = BASE_URL + url
        return self.ul_downloader.get(download_url)

    def parse_classify(self, htmlsource, header):
        bs = bs4.BeautifulSoup(htmlsource, "lxml")
        up_data = bs.findAll(class_='table-list-peo')
        down_data = bs.findAll(class_='table-list-info')
        results = []
        for index in range(len(up_data)):
            storage_data = {'peo':[], 'info':[]}
            index_bs = up_data[index]
            storage_data['html'] = index_bs.prettify()
            checkbox = index_bs.find(class_='checkbox')
            storage_data['id'] = checkbox['value']
            storage_data['date'] = time.time()
            storage_data['data-name'] = checkbox['data-name']
            storage_data['data-userid'] = checkbox['data-userid']
            storage_data['recommend'] = \
                index_bs.find(class_='icons16 icons16-recommend') is not None
            storage_data['elite'] = \
                index_bs.find(class_='icons16 icons16-elite') is not None
            mark = index_bs.find(class_='mark')
            storage_data['name'] = mark.text
            storage_data['href'] = mark['href']
            storage_data['title'] = mark['title']
            storage_data['data-id'] = mark['data-id']
            for td in up_data[index].findAll('td'):
                info = utils.tools.replace_tnr(td.text)
                if info:
                    storage_data['peo'].append(info)
            for td in down_data[index].findAll('td'):
                if info:
                    storage_data['info'].append(td.text)
            storage_data['tags'] = {}
            for index in header['tags'].keys():
                storage_data['tags'][index] = set()
                storage_data['tags'][index].add(header['tags'][index])
            results.append(storage_data)
        return results

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        side = bs.find(class_='side')
        side.decompose()
        footer = bs.find('footer')
        footer.decompose()
        javascripts = bs.findAll('script')
        for js in javascripts:
            js.decompose()
        alinks = bs.findAll('a')
        for a in alinks:
            a.decompose()
        content = bs.find(class_='resume')
        return content.prettify()

    def classify(self, postdata, header):
        htmlsource = self.urlget_classify(postdata)
        result = self.parse_classify(htmlsource, header)
        if len(result) == 0:
            if '没有找到符合' in result:
                result = None
            else:
                self.logException(htmlsource)
        return result

    def cv(self, url):
        download_url = self.BASE_URL + url
        htmlsource = self.wb_downloader.getsource(download_url)
        if u'处于猎聘网系统审核中' in htmlsource:
            raise NocontentCVException
        else:
            result = self.parse_cv(htmlsource)
        return result
