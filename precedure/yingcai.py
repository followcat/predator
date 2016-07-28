# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import time
import datetime
import re
import bs4
import json
import urllib
import math

import utils.tools
import utils.builtin
import precedure.base
import downloader._urllib
import downloader.webdriver
import storage.fsinterface
import storage.jobtitles

from sources.yingcai_all import *
from sources.yingcai_needed import *

class Yingcai(precedure.base.Base):

    BASE_URL=''
    FF_PROFILE_PATH_LIST=['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                          '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                          '/home/winky/.mozilla/firefox/4idae7t.winky3'
                         ]
    profilepath_index=0
    FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]
    START_TIME=datetime.datetime.now()

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

    def cv(self,url,profile_path):
        download_url=self.BASE_URL+url
        if profile_path==None:
            htmlsource=self.wb_downloader.getsource(download_url)
        else:
            self.wb_downloader.close()
            wbdriver_downloader = downloader.webdriver.Webdriver(profilepath=profile_path)
            yingcai=Yingcai(wbdownloader=wbdriver_downloader)
            htmlsource=self.wb_downloader.getsource(download_url)
        result=self.parse_cv(htmlsource)
        return result

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

def get_classify():
    wbdriverdownloader = downloader.webdriver.Webdriver(profilepath=Yingcai.FF_PROFILE_PATH)
    repo = storage.fsinterface.FSInterface('yingcai')
    repojt = storage.jobtitles.JobTitles(repo)
    yingcai=Yingcai(wbdownloader=wbdriverdownloader)
    live_places=[
            '18',#安徽
            '44',#澳门特别行政区
            '34',#北京
            '37',#重庆
            '19',#福建
            '31',#甘肃
            '25',#广东
            '38',#广西壮族自治区
            '28',#贵州
            '26',#海南
            '45',#海外
            '11',#河北
            '22',#河南
            '15',#黑龙江
            '23',#湖北
            '24',#湖南
            '14',#吉林
            '16',#江苏
            '20',#江西
            '13',#辽宁
            '39',#内蒙古自治区
            '41',#宁夏回族自治区
            '32',#青海
            '21',#山东
            '30',#陕西
            '12',#山西
            '36',#上海
            '27',#四川
            '33',#台湾
            '35',#天津　
            '40',#西藏自治区
            '43',#香港特别行政区
            '42',#新疆维吾尔自治区
            '29',#云南
            '17',#浙江
            ]
    for industry in job_list.keys():
        if len(job_list[industry].keys())==0:
            for key in industry_list[industry]:
                job_list[industry][key]=industry_list[indystry][key]
        for job in job_list[industry].keys():
            if len(job_list[industry][job])==0:
                job_list[industry][job]=industry_list[industry][job]
            for position in job_list[industry][job]:
                job_item=industry+','+job+','+position
                print job_item
                live_lists=[]
                chunk_len=5
                place_chunk=math.ceil(len(live_places)/chunk_len)
                for place_index in range(int(place_chunk)):
                    live=''
                    for index in range(chunk_len-1):
                        live+=(live_places[place_index*chunk_len+index]+';')
                    live=live+(live_places[place_index*chunk_len+index+1])
                    live_lists.append(live)

                block_size=10
                tot_block=15
                for live_index in range(0,len(live_lists)):
                    live_place=live_lists[live_index]
                    print live_place
                    getdict = {
                        'jobType':1,
                        'live':live_place,
                        'jobs':job_item,
                        'page':'0'
                         }
                    for index in range(0,tot_block):
                        minpage=index*block_size
                        maxpage=(index+1)*block_size
                        add_list=yingcai.update_classify(getdict,industry,repojt,minpage,maxpage)
                        if len(add_list)==0:
                            break
                        else:
                            id_str = industry
                            repojt.add_datas(id_str, add_list, 'winky')

                        current_time=datetime.datetime.now()
                        duration=(current_time-Yingcai.START_TIME).seconds
                        if duration > 1800:
                            wbdriverdownloader.close()
                            Yingcai.profilepath_index+=1
                            Yingcai.FF_PROFILE_PATH=Yingcai.FF_PROFILE_PATH_LIST[Yingcai.profilepath_index%len(Yingcai.FF_PROFILE_PATH_LIST)]
                            Yingcai.START_TIME=current_time
                            get_classify()
                        else:
                            continue


if __name__ == '__main__':
    get_classify()
