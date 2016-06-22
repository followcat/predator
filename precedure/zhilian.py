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
        'AdegreeMin':2,
        'AdegreeMax':9,
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

    def __init__(self, url_downloader=None, wbdownloader=None):
        self.url_downloader = url_downloader
        self.webdriver_downloader = wbdownloader

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
        download_url = 'http://h.highpin.cn' + url
        print 'download url: ' + download_url
        htmlsource = self.webdriver_downloader.getsource(download_url)
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
        if len(result) == 0:
            if '抱歉没有找到当前搜索条件的相关结果' in htmlsource:
                result = None
            else:
                self.logException(htmlsource)
        return result

    def cv(self, url):
        htmlsource = self.webdriverget_cv(url)
        result = self.parse_cv(htmlsource)
        return result

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception

    def update_classify(self, paramsdict, repojt, MIN_PAGE=0, MAX_PAGE=100, sleeptime=5):
        add_list = []
        id_str = paramsdict['JobType']
        for cur_page in range(MIN_PAGE, MAX_PAGE):
            paramsdict['PageIndex'] = cur_page + 1
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
        repojt.add_datas(id_str, add_list, 'kabess')
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
    industry_list = [
        # ['129900', '大型设备/机电设备/重工业'],
        # ['121200', '仪器仪表及工业自动化'],
        # ['300000', '航空/航天研究与制造'],
        # ['150000', '交通/运输/物流'],
        # ['121500', '医疗设备/器械'],
        # ['210500', '互联网/移动互联网/电子商务'],
        # ['160400', '计算机软件'],
        # ['160000', 'IT服务（系统/数据/维护）'],
        # ['160500', '电子技术/半导体/集成电路'],
        # ['160200', '计算机硬件及网络设备'],
        # ['300100', '通信/电信（设备/运营/增值）'],
        ['121100', '加工制造（原料加工/模具）'],
        ['121300', '医药/生物工程'],
        ['130100', '电气/电力/水利'],
        ['120600', '学术/科研'],
        ['200300', '专业服务(咨询/财会/法律/翻译等)'],
        ['201300', '检验/检测/认证'],
        ['201400', '中介服务/外包服务']
    ]
    jobtype_list = [
        ['160000', '全部(计算机/网络技术)'],
        ['410', '测试/可靠性工程师(电子/电气/半导体/仪器仪表)'],
        ['684', '射频工程师(电子/电气/半导体/仪器仪表)'],
        ['409', '项目管理/产品管理(电子/电气/半导体/仪器仪表)'],
        ['528', '研发工程师(电子/电气/半导体/仪器仪表)'],
        ['84', 'FAE现场应用工程师(电子/电气/半导体/仪器仪表)'],
        ['687', '嵌入式软件开发(Linux/单片机/DLC/DSP）(电子/电气/半导体/仪器仪表)'],
        ['407', '嵌入式硬件/软件工程师(电子/电气/半导体/仪器仪表)'],
        ['401', '设备工程师（调试/安装/维护）(电子/电气/半导体/仪器仪表)'],
        ['319', '机电工程师(电子/电气/半导体/仪器仪表)'],
        ['33', '自动化工程师(电子/电气/半导体/仪器仪表)'],
        ['467', '电气设计(电子/电气/半导体/仪器仪表)'],
        ['685', '工艺工程师(电子/电气/半导体/仪器仪表)'],
        ['249', '质量管理/测试经理(QA/QC经理)(质量管理/安全防护)'],
        ['250', '质量管理/测试主管(QA/QC主管)(质量管理/安全防护)'],
        ['251', '质量管理/测试工程师(QA/QC工程师)(质量管理/安全防护)'],
        ['253', '认证/体系工程师/审核员(质量管理/安全防护)'],
        ['295', '产品研发/注册(生物/制药/医疗器械)'],
        ['90', '技术文档工程师(工程机械)'],
        ['332', '工程机械经理/主管(工程机械)'],
        ['729', '工程/设备经理(工程机械)'],
        ['583', '工程/设备工程师(工程机械)'],
        ['584', '技术研发工程师(工程机械)'],
        ['732', '机电工程师(工程机械)'],
        ['734', '飞机维修机械师(工程机械)'],
        ['735', '飞行器设计与制造(工程机械)'],
        ['65', '生产总监/经理/车间主任(生产/加工/制造)'],
        ['63', '项目经理/主管(生产/加工/制造)'],
        ['66', '质量管理(生产/加工/制造)'],
        ['64', '生产主管/督导/组长(生产/加工/制造)'],
        ['72', '产品开发/技术/工艺(生产/加工/制造)'],
        ['735', '飞行器设计与制造(生产/加工/制造)'],
        ['245', '航空/列车/船舶操作维修(交通/物流/仓储)'],
        ['595', '飞机/列车/船舶设计与制造(交通/物流/仓储)'],
        # ['290', '核力/火力工程师(能源/矿产/地质勘查)'],
        # ['286', '电力工程师/技术员(能源/矿产/地质勘查)'],
        # ['158', '市场总监(市场/营销)'],
        # ['600', '市场经理/主管(市场/营销)'],
        # ['168', '品牌经理/主管(市场/营销)'],
        # ['7001000', '全部(销售管理/支持)'],
        # ['200', '财务总监(财务/审计/税务)'],
        # ['201', '财务经理(财务/审计/税务)'],
        # ['120', '人力资源总监(人力资源)'],
        # ['121', '人力资源经理/主管(人力资源)'],
        # ['128', '猎头顾问/助理(人力资源)'],
        # ['255', '科研人员(公务员/事业单位/科研机构)']
    ]
    for industry_item in industry_list:
        print '抓取的行业：' + str(industry_item[1])
        for jobtype_item in jobtype_list:
            print "正在抓取的职位: " + str(jobtype_item[1])
            paramsdict = {
                'CompanyIndustry':industry_item[0],
                'JobType':jobtype_item[0],
                'PageIndex': 0
            }
            zhilian.update_classify(paramsdict, repojt)


if __name__ == '__main__':
    get_classify()
