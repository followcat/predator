import urllib
import urllib2

import downloader.tools

def classify_postdata(update_dict):
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
    post_data.update(update_dict)
    return post_data

def classify_search(data):
    cookies_str = downloader.tools.getcookies()
    searchurl = 'https://h.liepin.com/cvsearch/soResume/'
    headers = {'Cookie': cookies_str}
    urllib_data = urllib.urlencode(data)
    req = urllib2.Request(searchurl, headers = headers)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    res = opener.open(req, urllib_data)
    text = res.read()
    return text


def cv(cv_url):
    cookies_str = downloader.tools.getcookies()
    CV_HREF = 'https://h.liepin.com'
    download_url = CV_HREF + cv_url
    headers = {'Cookie': cookies_str}
    req = urllib2.Request(download_url, headers = headers)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    res = opener.open(req)
    text = res.read()
    return text