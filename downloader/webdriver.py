import socket
import selenium.webdriver


class Webdriver(object):

    def __init__(self, profilepath=None):
        self.profilepath = profilepath
        profile = self.create_ff_profile()
        self.driver =  selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)

    def create_ff_profile(self):
        if self.profilepath is None:
            profile = None
        else:
            profile = selenium.webdriver.FirefoxProfile(self.profilepath)

    def getsource(self, url):
        try:
            self.driver.get(url)
        except socket.error:
            self.driver.quit()
            profile = self.create_ff_profile()
            self.driver = selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)
            self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
