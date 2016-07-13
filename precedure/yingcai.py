# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import time
import re
import bs4
import json
import urllib

import utils.tools
import utils.builtin
import precedure.base
import downloader._urllib
import downloader.webdriver
import storage.fsinterface
import storage.jobtitles

class Yingcai(precedure.base.Base):
	
    #get_data={
    #         'gtid':'4965e9b4-55e3-45de-a39b-c459163eae54'
    #         }
	
    def __init__(self, url_downloader=None, wbdownloader=None):
        self.url_downloader = url_downloader
        self.webdriver_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_data = dict()
       #tmp_data.update(self.get_data)
        tmp_data.update(data)
        searchurl = 'http://qy.chinahr.com/cv/sou?'
        params_str = urllib.urlencode(tmp_data)
        download_url = searchurl + params_str
        print 'download url: ' + download_url
        #return self.url_downloader.get(download_url)
        return self.webdriver_downloader.getsource(download_url)
        
    def webdriverget_cv(self, url):
        download_url = 'http://qy.chinahr.com/cv/sou?' + url
        print 'download url: ' + download_url
        htmlsource = self.webdriver_downloader.getsource(download_url)
        return htmlsource    
   
    def parse_classify(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        data_lists = bs.findAll(class_='searchChild')
        result = []
        for index in range(len(data_lists)):
            storage_data = { 'peo': [], 'info': [] }
            storage_data['date'] = time.time()
            storage_data['recommend'] = ''
            storage_data['elite'] = ''
            storage_data['name'] = ''
            storage_data['data-name'] = ''
            storage_data['data-id'] = ''
            cur_situation = data_lists[index]
            #print cur_situation
            abstract = data_lists[int(index)]
            #print abstract
            storage_data['html'] = cur_situation.prettify() + abstract.prettify()
            if cur_situation.find("a") is not None:
                element_a=cur_situation.find("a")
                storage_data['href'] = element_a.get('href')
                #print storage_data['href']
            query_str = utils.tools.queryString(element_a.get('href'))
            idmatch=re.search(r'cvid=(\w+)&from',cur_situation.find("a").get('href'))
            print idmatch.group(1)
            storage_data['id']=idmatch.group(1)
            peo_list = cur_situation.findAll(class_='rInfo1')
            #print peo_list
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
                #print storage_data
            info_list = abstract.find_all("p")
            #print info_list
            for info_item in info_list:
                storage_data['info'].append(info_item.text)
            result.append(storage_data)
        return result
 
    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def classify(self, params_data):
        htmlsource = self.urlget_classify(params_data)
        #print htmlsource
        #htmlsource = self.webdriverget_cv()
        htmlfile=open('/home/winky/predator/html','w')
        htmlfile.write(htmlsource)
        htmlfile.close()
        result = self.parse_classify(htmlsource)
        if len(result) == 0:
            if '抱歉没有找到当前搜索条件的相关结果' in htmlsource:
                result = None
            else:
                self.logException(htmlsource)
        return result

    def update_classify(self, paramsdict, repojt, MIN_PAGE=0, MAX_PAGE=150, sleeptime=5):
        add_list = []
        id_str = paramsdict['jobs']
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
        repojt.add_datas(id_str, add_list, 'winky')
        return True

def get_classify():
    #cookies_str = utils.builtin.loadfile('cookies.data')
    #urldownloader = downloader._urllib.Urllib()
    #urldownloader.set_cookies(cookies_str)
    profile_path='/home/winky/.mozilla/firefox/jvqqz5ch.winky'
    wbdriverdownloader = downloader.webdriver.Webdriver(profilepath=profile_path)
    #print urldownloader.get(url,True)
    repo = storage.fsinterface.FSInterface('yingcai')
    repojt = storage.jobtitles.JobTitles(repo)
    #yingcai= Yingcai(url_downloader=urldownloader)
    yingcai=Yingcai(wbdownloader=wbdriverdownloader)
    jobs_list=[
           '1001', #计算机／互联网／通信／电子发
           '1002', #销售／客服／技术支持
           '1003', #会计／金融／银行／保险
           '1004', #生产／营运／采购／物流
           '1005', #生物／制药／医疗／护理
           '1006', #广告／市场／媒体／艺术
           '1007', #建筑／房地产
           '1008', #人事／行政／高级管理
           '1009', #咨询／法律／教育／科研
           '1010', #服务业
           '1011', #公务员／翻译／其它
            ]
    for job_item in jobs_list:
        print job_item
        getdict = {
                   'live':'25,291',
                   'jobs':job_item, 
                   'page':'0'
		  }
	yingcai.update_classify(getdict,repojt)
	
if __name__ == '__main__':
    get_classify()
