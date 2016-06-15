import urllib
import urllib2

import downloader.tools
import selenium.webdriver


def classify_postdata():
    get_data = {
        'Q':'',
        'IsJobTitleOnly':'false',
        'IsPartialMatch':'false',
        'CompanyName':'',
        'IsArecent':'false',
        'CompanyIndustry':121500,
        'JobType':121300,
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
        'PageIndex':1,
        'PageSize':30,
        'Sort':'scoe desc',
        'IsAbstract':'true',
    }
    return get_data


def classify_search(data):
    cookies_str = downloader.tools.getcookies().replace("\n", "")
    searchurl = 'http://h.highpin.cn/SearchResume/SearchResumeList?'
    headers = {'Cookie': cookies_str}
    url_params = urllib.urlencode(data)
    req = urllib2.Request(searchurl+url_params, headers=headers)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    res = opener.open(req)
    text = res.read()
    return text


class Webdriver(object):

    def __init__(self, profilepath=None):
        if profilepath is None:
            profile = None
        else:
            profile = selenium.webdriver.FirefoxProfile(profilepath)
        self.driver =  selenium.webdriver.Firefox(firefox_profile=profile)

    def cv(self, cv_url):
        CV_HREF = 'http://h.highpin.cn/'
        download_url = CV_HREF + cv_url
        self.driver.get(download_url)
        return self.driver.page_source
