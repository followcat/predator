import selenium.webdriver


class Webdriver(object):

    def __init__(self, profilepath=None):
        if profilepath is None:
            profile = None
        else:
            profile = selenium.webdriver.FirefoxProfile(profilepath)
        self.driver =  selenium.webdriver.Firefox(firefox_profile=profile)

    def cv(self, cv_url):
        CV_HREF = 'https://h.liepin.com'
        download_url = CV_HREF + cv_url
        self.driver.get(download_url)
        return self.driver.page_source