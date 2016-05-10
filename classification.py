# -*- coding: utf-8 -*-

import time
import urllib
import urllib2

import bs4

import utils.tools
import interface.gitinterface
import interface.repojobtitles
from sources.datajobs import *


def getcookies():
    cookies_str = ''
    with open('cookies.data') as fp:
        cookies_str = fp.read()
    return cookies_str

def classify_search(data, cookies_str):
    searchurl = 'https://h.liepin.com/cvsearch/soResume/'
    headers = {'Cookie': cookies_str}
    urllib_data = urllib.urlencode(data)
    req = urllib2.Request(searchurl, headers = headers)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    res = opener.open(req, urllib_data)
    text = res.read()
    return text

def catchman(htmlsource):
    bs = bs4.BeautifulSoup(htmlsource)
    up_data = bs.findAll(class_='table-list-peo')
    down_data = bs.findAll(class_='table-list-info')
    results = []
    for index in range(len(up_data)):
        storage_data = {'peo':[], 'info':[]}
        index_bs = up_data[index]
        checkbox = index_bs.find(class_='checkbox')
        storage_data['id'] = checkbox['value']
        storage_data['data-name'] = checkbox['data-name']
        storage_data['data-userid'] = checkbox['data-userid']
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
        results.append(storage_data)
    return results

def logException(text):
    with open('/tmp/runner.log', 'a+') as fp:
        fp.write(text)
    raise Exception

post_data = {
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

if __name__ == '__main__':
    cookies_str = getcookies()
    repo = interface.gitinterface.GitInterface('data')
    jt = interface.repojobtitles.JobTitles(repo)
    for id_str in localdatajobs['jobtitles']:
        try:
            int_id = int(id_str)
        except ValueError:
            continue
        if len(id_str) > 3:
            post_data['jobtitles'] = id_str
            print localdatajobs['jobtitles'][id_str][0]
            add_list = []
            for curPage in range(100):
                post_data['curPage'] = curPage + 1
                text = classify_search(post_data, cookies_str)
                results = catchman(text)
                if len(results) == 0:
                    if '没有找到符合' in text:
                        break
                    else:
                        logException(text)
                parts_results = []
                for result in results:
                    if not jt.exists(id_str, result['id']):
                        parts_results.append(result)
                print curPage
                if len(parts_results) < len(results)*0.2:
                    break
                else:
                    add_list.extend(parts_results)
            jt.add_datas(id_str, add_list, 'followcat')
            break
