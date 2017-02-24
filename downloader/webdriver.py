import socket
import selenium.webdriver


def create_ff_profile(profile_path):
    if profile_path is None:
        profile = None
    else:
        profile = selenium.webdriver.FirefoxProfile(profile_path)
    return profile


class Webdriver(object):

    def __init__(self, profilepath=None):
        self.profilepath = profilepath
        profile = create_ff_profile(self.profilepath)
        self.driver =  selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)

    def getsource(self, url):
        try:
            self.driver.get(url)
        except socket.error:
            self.driver.quit()
            profile = create_ff_profile(self.profilepath)
            self.driver = selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)
            self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
