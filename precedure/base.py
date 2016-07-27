class NotImplementedInterface(Exception):
    pass

class Base(object):

    BASE_URL=''

    def __init__(self):
        self.url_downloader = url_downloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self):
        raise NotImplementedInterface

    def urlget_cv(self):
        raise NotImplementedInterface

    def webdriverget_classify(self):
        raise NotImplementedInterface

    def webdriverget_cv(self):
        raise NotImplementedInterface

    def parse_classify(self):
        raise NotImplementedInterface

    def parse_cv(self):
        raise NotImplementedInterface

    def classify(self):
        raise NotImplementedInterface

    def cv(self,url):
        download_url=self.BASE_URL+url
        htmlsource=self.wb_downloader.getsource(download_url)
        result=self.parse_cv(htmlsource)
        return result
