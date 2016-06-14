import utils.builtin
import downloader.urllib


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
    cookies_str = utils.builtin.loadfile('cookies.data')
    dl_url = downloader.urllib.Urllib()
    dl_url.set_cookies(cookies_str)
    searchurl = 'https://h.liepin.com/cvsearch/soResume/'
    return dl_url.post(searchurl, data=data)

def cv(cv_url):
    cookies_str = utils.builtin.loadfile('cookies.data')
    dl_url = downloader.urllib.Urllib()
    dl_url.set_cookies(cookies_str)
    download_url = 'https://h.liepin.com' + cv_url
    return dl_url.get(download_url)


