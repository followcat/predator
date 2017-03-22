import socket
import selenium.webdriver
import selenium.common.exceptions

from selenium.webdriver.common.keys import Keys


def create_firefox_driver(profile_path):
    if profile_path is None:
        profile = None
    else:
        profile = selenium.webdriver.FirefoxProfile(profile_path)
    driver =  selenium.webdriver.Firefox(firefox_profile=profile, timeout=600)
    current_handler = driver.window_handles[-1]
    return driver, current_handler

def create_new_window(downloader):
    driver = downloader.driver
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 'n')
    current_handler = driver.window_handles[-1]
    driver.switch_to.window(current_handler)
    return current_handler


class Webdriver(object):

    def __init__(self, profilepath=None, downloader=None):
        self.handler = None
        self.profilepath = None
        if downloader is not None:
            self.handler = create_new_window(downloader)
            self.driver = downloader.driver
        else:
            self.profilepath = profilepath
            self.driver, self.handler =  create_firefox_driver(self.profilepath)

    def switch_profile(self, profile_paths):
        if self.profilepath is None:
            return
        if self.profilepath in profile_paths:
            index = profile_paths.index(self.profilepath)
            next_index = (index + 1)%len(profile_paths)
            self.profilepath = profile_paths[next_index]
        else:
            self.profilepath = profile_paths[0]
        tmp_driver, tmp_handler =  create_firefox_driver(self.profilepath)
        tmp_driver.get(self.driver.current_url)
        self.driver.delete_all_cookies()
        for cookie in tmp_driver.get_cookies():
            try:
                self.driver.add_cookie(cookie)
            except selenium.common.exceptions.WebDriverException:
                continue
        tmp_driver.quit()

    def getsource(self, url):
        try:
            self.driver.switch_to_window(self.handler)
            self.driver.get(url)
        except socket.error:
            self.driver.quit()
            self.driver = create_firefox_driver(self.profilepath)
            self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
