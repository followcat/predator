# -*- coding: utf-8 -*-
import glob
import os.path
import time
import bs4
import urllib

import utils.tools
import utils.builtin
import downloader.webdriver
import precedure.base
import precedure.zhilian


class Zhilian(precedure.base.Base):

    urls_data = {
        'Q':'',
        'IsJobTitleOnly':'false',
        'IsPartialMatch':'false',
        'CompanyName':'',
        'IsArecent':'false',
        'DesiredWorkLocation':'',
        'JobLocation':'',
        'AdegreeMin':-1,
        'AdegreeMax':-1,
        'WorkExperienceMin':-1,
        'WorkExperienceMax':-1,
        'AgeMin':'',
        'AgeMax':'',
        'Gender':-1,
        'Language':-1,
        'Language1':-1,
        'Ability1':-1,
        'Language2':-1,
        'Ability2':-1,
        'Language3':-1,
        'Ability3':-1,
        'OverseasJobExperience':-1,
        'WorkStatus':-1,
        'SchoolName':'',
        'ProfessionalTitle':'',
        'PageSize':30,
        'Sort':'scoe desc',
        'IsAbstract':'true',
    }

    def __init__(self, url_downloader=None, webdriver_downloader=None):
        self.url_downloader = url_downloader
        self.webdriver_downloader = webdriver_downloader

    def urlget_classify(self, data):
        tmp_data = dict()
        tmp_data.update(self.urls_data)
        tmp_data.update(data)
        searchurl = 'http://h.highpin.cn/SearchResume/SearchResumeList?'
        params_str = urllib.urlencode(tmp_data)
        download_url = searchurl + params_str
        print 'download url: ' + download_url
        return self.url_downloader.get(download_url)

    def urlget_cv(self, url):
        download_url = 'http://h.highpin.cn' + url
        print 'download url: ' + download_url
        return self.url_downloader.get(download_url)

    def webdriverget_cv(self, url):
        htmlsource = self.webdriver_downloader.getsource(url)
        return htmlsource

    def parse_classify(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        data_lists = bs.findAll(class_='bor-bottom')
        result = []
        for index in range(1, len(data_lists), 2):
            storage_data = { 'peo': [], 'info': [] }
            storage_data['date'] = time.time()
            storage_data['recommend'] = ''
            storage_data['elite'] = ''
            storage_data['name'] = ''
            storage_data['data-name'] = ''
            storage_data['data-id'] = ''
            cur_situation = data_lists[index]
            abstract = data_lists[int(index+1)]
            storage_data['html'] = cur_situation.prettify() + abstract.prettify()
            peo_list = cur_situation.findAll(class_='list-three')
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
            info_list = abstract.find_all("p")
            for info_item in info_list:
                storage_data['info'].append(info_item.text)
            result.append(storage_data)
        return result

    def parse_cv(self, htmlsource):
        bs = bs4.BeautifulSoup(htmlsource, 'lxml')
        recommand = bs.find(id='recommand-btn-area')
        recommand.decompose()
        send_contact = bs.find(id='haveSeenContact')
        send_contact.decompose()
        contact_type = bs.find(id='showContactType')
        contact_type.decompose()
        label = bs.find(class_='evalListsInnerBox')
        label_link = label.findAll('a')
        for e in label_link:
            e.decompose()
        detail_content = bs.find(class_='detail-con')
        resume_content = bs.find(class_='detail-tabs-new')
        return detail_content.prettify() + resume_content.prettify()

    def classify(self, params_data):
        htmlsource = self.urlget_classify(params_data)
        result = self.parse_classify(htmlsource)
        return result

    def cv(self, url):
        htmlsource = self.urlget_cv(url)
        result = self.parse_cv(htmlsource)
        return result

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def update_classify(self, paramsdict, repojt, MAX_PAGE=2, sleeptime=10):
        add_list = []
        id_str = paramsdict['JobType']
        for cur_page in range(MAX_PAGE):
            paramsdict['PageIndex'] = cur_page + 1
            results = self.classify(paramsdict)
            if len(results) == 0:
                if '没有找到符合' in text:
                    break
                else:
                    self.logException(text)
            parts_results = []
            for result in results:
                if not repojt.exists(id_str, result['id']):
                    parts_results.append(result)
            print 'current page:' + str(cur_page)
            if len(parts_results) < len(results)*0.2:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(sleeptime)
        repojt.add_datas(id_str, add_list, 'kabess')
        return True


    def update_cv(self, repojt, repocv, sleeptime=10):
        for pathfile in glob.glob(os.path.join(repojt.repo_path, '*.yaml')):
            path, name = os.path.split(pathfile)
            yamldata = utils.builtin.load_yaml(path, name)
            for cv_id in yamldata:
                if repocv.exists(cv_id):
                    continue
                cv_info = yamldata[cv_id]
                cv_href = cv_info['href']
                cv_content = self.cv(cv_href)
                repocv.add(cv_id, cv_content.encode('utf-8'), 'kabess')
                print 'current cv id: ' + str(cv_id)
                time.sleep(sleeptime)
        return True


def get_classify():
    import downloader._urllib
    import storage.gitinterface
    import storage.repojobtitles
    cookies_str = utils.builtin.loadfile('zhiliancookie.data').replace('\n','')
    urldownloader = downloader._urllib.Urllib()
    urldownloader.set_cookies(cookies_str)
    webdriverdownloader = downloader.webdriver.Webdriver()
    repo = storage.gitinterface.GitInterface('zhilian')
    repojt = storage.repojobtitles.JobTitles(repo)
    zhilian = precedure.zhilian.Zhilian(url_downloader=urldownloader)
    paramsdict = {
        'CompanyIndustry':121500,
        'JobType':121300,
        'PageIndex':1
    }
    zhilian.update_classify(paramsdict, repojt)


def get_cv():
    import downloader._urllib
    import storage.gitinterface
    import storage.repojobtitles
    import storage.repocv
    cookies_str = utils.builtin.loadfile('zhiliancookie.data').replace('\n','')
    urldownloader = downloader._urllib.Urllib()
    urldownloader.set_cookies(cookies_str)
    repo = storage.gitinterface.GitInterface('zhilian')
    repojt = storage.repojobtitles.JobTitles(repo)
    cv_repo = storage.gitinterface.GitInterface('zhilian_cv')
    repocv = storage.repocv.CurriculumVitae(cv_repo)
    zhilian = precedure.zhilian.Zhilian(url_downloader=urldownloader)
    zhilian.update_cv(repojt, repocv)

if __name__ == '__main__':
    get_classify()
    get_cv()
