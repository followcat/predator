# -*- coding: utf-8 -*-

import time

import bs4
import json

import utils.tools
import utils.builtin
import precedure.base
import downloader._urllib
import storage.fsinterface
import storage.jobtitles

from sources.jingying import *


class Jingying(precedure.base.Base):

    BASE_URL='http://www.51jingying.com'

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

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def update_classify(self, id_str, postdict, repojt, MAX_PAGE=20, sleeptime=10):
        add_list = []
        for curPage in range(MAX_PAGE):
            postdict['curr_page'] = curPage + 1
            results = self.classify(postdict)
            if len(results) == 0:
                break
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
    repo = storage.fsinterface.FSInterface('jingying')
    repojt = storage.jobtitles.JobTitles(repo)
    jingying = Jingying(uldownloader=ul_downloader)
    #start from industry
    industry_list = [
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
    for id_str in industry_list:
        print localdatajobs['industry'][id_str]
        postdict = {'indtype': id_str,
                    'curr_page': '0'}
        jingying.update_classify(id_str, postdict, repojt)

    #Then go on with company names group by area
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
    for _area in company_area_list:
        for c_name in localdatajobs['company_name'][_area]:
            print c_name
            postdict = {'cotext': c_name.decode('utf-8').encode('gb2312'),
                        'curr_page': '0'}
            jingying.update_classify(_area, postdict, repojt)


if __name__ == '__main__':
    get_classify()
