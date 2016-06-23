import selenium.webdriver


class Webdriver(object):

    def __init__(self, profilepath=None):
        if profilepath is None:
            profile = None
        else:
            profile = selenium.webdriver.FirefoxProfile(profilepath)
        self.driver =  selenium.webdriver.Firefox(firefox_profile=profile)

    def getsource(self, url):
        self.driver.get(url)
        return self.driver.page_source
