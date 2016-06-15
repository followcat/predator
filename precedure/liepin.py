# -*- coding: utf-8 -*-

import time

import utils.builtin
import htmlparser.liepin
import downloader.urllib

class Liepin(object):

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

    def __init__(self):
        self.cookies_str = utils.builtin.loadfile('cookies.data')
        self.ul_downloader = downloader.urllib.Urllib()
        self.ul_downloader.set_cookies(self.cookies_str)

    def classify(self, data):
        tmp_post = dict()
        tmp_post.update(self.post_data)
        tmp_post.update(data)
        searchurl = 'https://h.liepin.com/cvsearch/soResume/'
        return self.ul_downloader.post(searchurl, data=tmp_post)

    def url_cv(self, url):
        download_url = 'https://h.liepin.com' + url
        return self.ul_downloader.get(download_url)

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def update_classify(self, postdict, repojt, MAX_PAGE=100, sleeptime=10):
        add_list = []
        id_str = postdict['jobtitles']
        for curPage in range(MAX_PAGE):
            post_data['curPage'] = curPage + 1
            text = self.classify(post_data)
            results = htmlparser.liepin.catchman(text)
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
        repojt.add_datas(id_str, add_list, 'followcat')
        return True


if __name__ == '__main__':
    import storage.gitinterface
    import storage.repojobtitles
    from sources.datajobs import *
    repo = storage.gitinterface.GitInterface('liepin')
    repojt = storage.repojobtitles.JobTitles(repo)
    liepin = precedure.liepin.Liepin()
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
    for id_str in selected:
        print localdatajobs['jobtitles'][id_str][0]
        postdict = {'industrys': 290,
                    'jobtitles': id_str,
                    'curPage': 0}
        liepin.update_classify(postdict, repojt)