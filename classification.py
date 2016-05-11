# -*- coding: utf-8 -*-

import time

import htmlparser.liepin
import downloader.liepin
import interface.gitinterface
import interface.repojobtitles
from sources.datajobs import *

def logException(text):
    with open('/tmp/classification.log', 'a+') as fp:
        fp.write(text)
    raise Exception

def update_jobtitle(id_str, repojt, MAX_PAGE=100):
    add_list = []
    post_data = downloader.liepin.classify_postdata({
                'jobtitles': id_str,
                'curPage': 0})
    for curPage in range(100):
        post_data['curPage'] = curPage + 1
        text = downloader.liepin.classify_search(post_data)
        results = htmlparser.liepin.catchman(text)
        if len(results) == 0:
            if '没有找到符合' in text:
                break
            else:
                logException(text)
        parts_results = []
        for result in results:
            if not repojt.exists(id_str, result['id']):
                parts_results.append(result)
        print curPage
        if len(parts_results) < len(results)*0.2:
            break
        else:
            add_list.extend(parts_results)
    repojt.add_datas(id_str, add_list, 'followcat')
    return True

def update_all_jobtitles(repojt):
    for id_str in localdatajobs['jobtitles']:
        try:
            int_id = int(id_str)
        except ValueError:
            continue
        if len(id_str) > 3:
            print localdatajobs['jobtitles'][id_str][0]
            update_jobtitle(id_str, repojt)

def updata_select_jobtitles(repojt, selected):
    for id_str in selected:
        print localdatajobs['jobtitles'][id_str][0]
        update_jobtitle(id_str, repojt)

if __name__ == '__main__':
    repo = interface.gitinterface.GitInterface('liepin')
    repojt = interface.repojobtitles.JobTitles(repo)
    update_all_jobtitles(repojt)
