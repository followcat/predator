import socket
import selenium.webdriver


def create_firefox_driver(profile_path):
    if profile_path is None:
        profile = None
    else:
        profile = selenium.webdriver.FirefoxProfile(profile_path)
    driver =  selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)
    return driver


class Webdriver(object):

    def __init__(self, profilepath=None):
        self.profilepath = profilepath
        self.driver =  create_firefox_driver(self.profilepath)

    def getsource(self, url):
        try:
            self.driver.get(url)
        except socket.error:
            self.driver.quit()
            self.driver =  create_firefox_driver(self.profilepath)
            self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
