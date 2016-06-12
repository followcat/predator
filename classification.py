# -*- coding: utf-8 -*-

import time

import htmlparser.liepin
import downloader.liepin
import storage.gitinterface
import storage.repojobtitles
from sources.datajobs import *

def logException(text):
    with open('/tmp/classification.log', 'a+') as fp:
        fp.write(text)
    raise Exception

def update_jobtitle(postdict, repojt, MAX_PAGE=100, sleeptime=10):
    add_list = []
    id_str = postdict['jobtitles']
    post_data = downloader.liepin.classify_postdata(postdict)
    for curPage in range(MAX_PAGE):
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
        time.sleep(sleeptime)
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

def update_select_jobtitles(repojt, selected):
    for id_str in selected:
        print localdatajobs['jobtitles'][id_str][0]
        postdict = {'industrys': 290,
                    'jobtitles': id_str,
                    'curPage': 0}
        update_jobtitle(postdict, repojt)

if __name__ == '__main__':
    repo = storage.gitinterface.GitInterface('liepin')
    repojt = storage.repojobtitles.JobTitles(repo)
    selected_list = [
    '290094', #医疗器械研发
    '290097', #医疗器械生产/质量管理
    '060010', #市场总监
    '020010', #销售总监
    '040020', #项目经理/主管
    '040040', #项目专员/助理
    '050010', #质量管理/测试经理(QA/QC经理)
    '050080', #体系工程师/审核员
    '050020', #质量管理/测试主管(QA/QC主管)
    ]
    update_select_jobtitles(repojt, selected_list)
