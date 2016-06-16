# -*- coding: utf-8 -*-

import time

import bs4
import json

import utils.tools
import utils.builtin
import precedure.base
import downloader._urllib
import storage.gitinterface
import storage.repojobtitles

from sources.jingying import *


class Jingying(precedure.base.Base):

    post_data = {
        'url': '/spy/searchmanager.php?act=getSpySearch',
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
        download_url = 'http://www.51jingying.com' + url
        return self.ul_downloader.get(download_url)

    def webdriverget_cv(self, url):
        download_url = 'http://www.51jingying.com' + url
        htmlsource = self.wb_downloader.getsource(download_url)
        return htmlsource

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

    def cv(self, url):
        htmlsource = self.webdriverget_cv(url)
        result = self.parse_cv(htmlsource)
        return result

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def update_classify(self, postdict, repojt, MAX_PAGE=20, sleeptime=10):
        add_list = []
        id_str = postdict['indtype']
        for curPage in range(MAX_PAGE):
            postdict['curr_page'] = curPage + 1
            results = self.classify(postdict)
            if len(results) == 0:
                if '没有找到符合' in text:
                    break
                else:
                    self.logException(text)
            parts_results = []
            for result in results:
                if not repojt.exists(id_str, result['id']):
                    parts_results.append(result)
            print curPage
            if len(parts_results) < len(results)*0.2:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(sleeptime)
        repojt.add_datas(id_str, add_list, 'zhangqunyun')
        return True


def get_classify():
    cookies_str = utils.builtin.loadfile('cookies.data').rstrip('\n')
    ul_downloader = downloader._urllib.Urllib()
    ul_downloader.set_cookies(cookies_str)
    repo = storage.gitinterface.GitInterface('jingying')
    repojt = storage.repojobtitles.JobTitles(repo)
    jingying = Jingying(uldownloader=ul_downloader)
    selected_list = [
    '47', #医疗设备/器械
    '01', #计算机软件
    '37', #计算机硬件
    '38', #计算机服务(系统、数据服务、维修)
    '31', #通信/电信/网络设备
    '35', #仪器仪表/工业自动化
    '14', #机械/设备/重工
    '52', #检测，认证
    '07', #专业服务(咨询、人力资源、财会)
    '24', #学术/科研
    '21', #交通/运输/物流
    '55', #航天/航空
    '36', #电气/电力/水利
    '55', #航天/航空
    '61', #新能源
    ]
    for id_str in selected_list:
        print localdatajobs['industry'][id_str]
        postdict = {'indtype': id_str,
                    'nisseniordb': 0, #0-高级人才库, 1-全部人才库, 2-御用精英人才库
                    'curr_page': '0'}
        jingying.update_classify(postdict, repojt)


if __name__ == '__main__':
    get_classify()
