# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re
import bs4
import json
import time

import utils.tools
import precedure.base
import urllib

class Yingcai(precedure.base.Base):

    BASE_URL=''

    def __init__(self, url_downloader=None, wbdownloader=None):
        self.url_downloader = url_downloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_data = dict()
        tmp_data.update(data)
        searchurl = 'http://qy.chinahr.com/cv/sou?'
        params_str = urllib.urlencode(tmp_data)
        download_url = searchurl + params_str
        print 'download url: ' + download_url
        return self.wb_downloader.getsource(download_url)
        
    def webdriverget_cv(self, url):
        download_url = 'http://qy.chinahr.com/cv/sou?' + url
        print 'download url: ' + download_url
        htmlsource = self.wb_downloader.getsource(download_url)
        return htmlsource

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        content = bs.find(class_='box-myResume')
        return content.prettify()

    def parse_classify(self, htmlsource):
        result = []
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        text_lists=bs.findAll(class_='searchList')
        if len(text_lists)==0:
            return result
        data_lists=text_lists[0].findAll("li")
        if len(data_lists)==0:
            return result
        else:
            for index in range(len(data_lists)):
                storage_data = { 'peo': [], 'info': [] }
                workyear_text= data_lists[index].find(class_='workYear').string
                yearmatch=re.search('(\d+).*',workyear_text)
                age_text=data_lists[index].find(class_='age').string
                agematch=re.search('(\d+).*',age_text)
                try:
                    workyear=int(yearmatch.group(1))
                    age=int(agematch.group(1))
                except Exception:
                    continue
                if workyear < 3 or age < 25:
                    continue
                storage_data['date'] = time.time()
                storage_data['recommend'] = ''
                storage_data['elite'] = ''
                storage_data['data-name'] = ''
                storage_data['data-id'] = ''
                storage_data['title']=''
                storage_data['data-userid']=''
                cur_situation = data_lists[index]
                storage_data['html'] = cur_situation.prettify()
                if cur_situation.find("a") is not None:
                    element_a=cur_situation.find("a")
                    storage_data['href'] = element_a.get('href')
                query_str = utils.tools.queryString(element_a.get('href'))
                storage_data['id']=data_lists[index].attrs['cvid']
                storage_data['name']=(data_lists[index].find(class_='name').string).decode('utf-8')
                storage_data['info'].append((data_lists[index].find(class_='sex').string).decode('utf-8'))
                storage_data['info'].append((data_lists[index].find(class_='age').string).decode('utf-8'))
                storage_data['info'].append((data_lists[index].find(class_='workYear').string).decode('utf-8'))
                storage_data['info'].append((data_lists[index].find(class_='edu').string).decode('utf-8'))
                update_text=data_lists[index].find(class_='source')
                update_time=update_text.find('em').getText()
                storage_data['info'].append(update_time)
                info_text=data_lists[index].find(class_='rInfo2')
                info_lists=info_text.findAll('span')
                for info_index in range(len(info_lists)):
                    storage_data['peo'].append(info_lists[info_index].getText())
                result.append(storage_data)
        return result
 
    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def classify(self, params_data):
        htmlsource = self.urlget_classify(params_data)
        result = self.parse_classify(htmlsource)
        if len(result) == 0:
            if '对不起，没有找到合适条件的简历' in htmlsource:
                result = None
            else:
                self.logException(htmlsource)
        return result

    def update_classify(self, paramsdict, industry,repojt, MIN_PAGE, MAX_PAGE, sleeptime=60):
        add_list = []
        id_str = industry
        for cur_page in range(MIN_PAGE, MAX_PAGE):
            paramsdict['page'] = cur_page + 1
            results = self.classify(paramsdict)
            if results is None:
                break
            parts_results = []
            for result in results:
               if not repojt.exists(id_str, result['id']):
                   parts_results.append(result)
            print 'current page:' + str(cur_page + 1)
            if len(parts_results) < len(results)*0.2:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(sleeptime)
        return add_list