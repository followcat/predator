# -*- coding: utf-8 -*-

import time
import json

import bs4

import utils.tools
import precedure.base


class Jingying(precedure.base.Base):

    BASE_URL='http://www.51jingying.com'
    PAGE_VAR = 'curr_page'
    CLASSIFY_SLEEP = 5
    CLASSIFY_MAXPAGE = 20

    post_data = {
        'nisseniordb': 1, #0-高级人才库, 1-全部人才库, 2-御用精英人才库
        'indtype': '',
        'potext': '',
        'cotext': '',
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
        self.setup()

    def setup(self):
        if self.wb_downloader:
            try:
                self.wb_downloader.driver.get(self.BASE_URL)
            except Exception:
                pass

    def urlget_classify(self, data):
        tmp_post = dict()
        tmp_post.update(self.post_data)
        tmp_post.update(data)
        searchurl = 'http://www.51jingying.com/spy/searchmanager.php?act=getSpySearch'
        ret = self.wb_downloader.getsource(searchurl, form=tmp_post)
        return ret

    def urlget_cv(self, url):
        download_url = BASE_URL + url
        return self.ul_downloader.get(download_url)

    def parse_classify(self, htmlsource, header):
        bs = bs4.BeautifulSoup(htmlsource, "lxml")
        items = bs.findAll('li', class_='')
        results = []
        for index in range(len(items)):
            storage_data = {'peo':[], 'info':[]}
            index_bs = items[index]
            storage_data['html'] = index_bs.prettify()
            storage_data['id'] = index_bs.get('objectoriginalid')
            storage_data['data-name'] = ''
            storage_data['date'] = time.time()
            storage_data['data-userid'] = ''
            storage_data['recommend'] = ''
            storage_data['elite'] = ''
            storage_data['name'] = ''
            storage_data['title'] = ''
            storage_data['data-id'] = ''
            label_list = index_bs.findAll('label')
            for index_lab in range(len(label_list)):
                if index_lab == 0:
                    storage_data['href'] = label_list[index_lab].find('a').get('href')
                    position =label_list[index_lab].find('span').getText()
                    storage_data['peo'].append(position)
                else:
                    content = label_list[index_lab].getText()
                    storage_data['peo'].append(content)
            date_text=index_bs.find(class_='yy_listButtom fl')
            date = date_text.find('p').getText()
            storage_data['peo'].append(date)
            storage_data['tags'] = {}
            for index in header['tags'].keys():
                storage_data['tags'][index] = set()
                storage_data['tags'][index].add(header['tags'][index])
            results.append(storage_data)
        return results

    def parse_cv(self, htmlsource):
        if u'您尚未通过招聘资质认证' in htmlsource:
            raise Exception("Account error")
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        content = bs.find(id='51jobcv')
        if content is None:
            content = bs.find(id='resume')
        style = content.find('style')
        if style is not None:
            style.decompose()
        meta = content.find('meta')
        if meta is not None:
            meta.decompose()
        return content.prettify()

    def classify(self, postdata, header):
        page = self.urlget_classify(postdata)
        try:
            json_res = json.loads(page)
            htmlsource = json_res['html']
        except KeyError:
            pass
        result = self.parse_classify(htmlsource, header)
        return result

    def update_classify(self, filename, id_str, postdict, repojt, add_list,
                        update_list, header=None, flush=True):
        for cur_page in range(self.CLASSIFY_MAXPAGE):
            postdict[self.PAGE_VAR] = cur_page + 1
            results = self.classify(postdict, header)
            if not results:
                break
            parts_results = []
            for result in results:
                if not repojt.exists(id_str, result['id']):
                    parts_results.append(result)
                else:
                    update_list.append(result)
            print 'current page:' + str(cur_page + 1)
            if len(parts_results) < len(results)*0.2:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(self.CLASSIFY_SLEEP)
        head = {}
        head['postdict'] = header['postdict']
        if flush and (len(add_list) > 0 or len(update_list) > 0):
            repojt.add_datas(filename, add_list, update_list, head)
        return True
