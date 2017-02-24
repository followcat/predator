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

    def switch_profile(self, profile_paths):
        self.close()
        if self.profilepath in profile_paths:
            index = profile_paths.index(self.profilepath)
            next_index = (index + 1)%len(profile_paths)
            self.profilepath = profile_paths[next_index]
        else:
            self.profilepath = profile_paths[0]
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
