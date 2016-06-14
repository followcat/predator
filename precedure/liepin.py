import utils.builtin
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
