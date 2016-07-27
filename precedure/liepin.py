# -*- coding: utf-8 -*-

import time

import bs4

import utils.tools
import utils.builtin
import precedure.base


class NocontentCVException(Exception):
    pass

class Liepin(precedure.base.Base):

    BASE_URL='https://h.liepin.com'

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

    def __init__(self, uldownloader=None, wbdownloader=None):
        self.ul_downloader = uldownloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self, data):
        tmp_post = dict()
        tmp_post.update(self.urls_post)
        tmp_post.update(data)
        searchurl = 'https://h.liepin.com/cvsearch/soResume/'
        return self.ul_downloader.post(searchurl, data=tmp_post)

    def urlget_cv(self, url):
        download_url = BASE_URL + url
        return self.ul_downloader.get(download_url)

    def parse_classify(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, "lxml")
        up_data = bs.findAll(class_='table-list-peo')
        down_data = bs.findAll(class_='table-list-info')
        results = []
        for index in range(len(up_data)):
            storage_data = {'peo':[], 'info':[]}
            index_bs = up_data[index]
            storage_data['html'] = index_bs.prettify()
            checkbox = index_bs.find(class_='checkbox')
            storage_data['id'] = checkbox['value']
            storage_data['date'] = time.time()
            storage_data['data-name'] = checkbox['data-name']
            storage_data['data-userid'] = checkbox['data-userid']
            storage_data['recommend'] = \
                index_bs.find(class_='icons16 icons16-recommend') is not None
            storage_data['elite'] = \
                index_bs.find(class_='icons16 icons16-elite') is not None
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

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        side = bs.find(class_='side')
        side.decompose()
        footer = bs.find('footer')
        footer.decompose()
        javascripts = bs.findAll('script')
        for js in javascripts:
            js.decompose()
        alinks = bs.findAll('a')
        for a in alinks:
            a.decompose()
        content = bs.find(class_='resume')
        return content.prettify()

    def classify(self, postdata):
        htmlsource = self.urlget_classify(postdata)
        result = self.parse_classify(htmlsource)
        if len(result) == 0:
            if '没有找到符合' in result:
                result = None
            else:
                self.logException(htmlsource)
        return result

    def cv(self, url):
        download_url = BASE_URL + url
        htmlsource = self.wb_downloader.getsource(download_url)
        if u'处于猎聘网系统审核中' in htmlsource:
            raise NocontentCVException
        else:
            result = self.parse_cv(htmlsource)
        return result

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception(text)

    def update_classify(self, postdict, repojt, MAX_PAGE=100, sleeptime=5):
        add_list = []
        id_str = postdict['jobtitles']
        for curPage in range(MAX_PAGE):
            postdict['curPage'] = curPage + 1
            try:
                results = self.classify(postdict)
            except Exception:
                break
            if results is None:
                break
            parts_results = []
            for result in results:
                if not repojt.exists(id_str, result['id']):
                    parts_results.append(result)
            print curPage
            if len(parts_results) < len(results)* 0.05:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(sleeptime)
        repojt.add_datas(id_str, add_list, 'followcat')
        return True


def get_classify():
    import downloader._urllib
    import storage.jobtitles
    import storage.gitinterface
    from sources.liepin import localdatajobs
    cookies_str = utils.builtin.loadfile('cookies.data')
    ul_downloader = downloader._urllib.Urllib()
    ul_downloader.set_cookies(cookies_str)
    repo = storage.gitinterface.GitInterface('liepin')
    repojt = storage.jobtitles.JobTitles(repo)
    liepin = Liepin(uldownloader=ul_downloader)
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
    for id_str in selected_list:
        print localdatajobs['jobtitles'][id_str][0]
        postdict = {'industrys': 290,
                    'jobtitles': id_str,
                    'curPage': 0}
        liepin.update_classify(postdict, repojt)


if __name__ == '__main__':
    get_classify()
