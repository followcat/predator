import socket
import threading
import selenium.webdriver
import selenium.common.exceptions

from selenium.webdriver.common.keys import Keys


class Driver(selenium.webdriver.Firefox):
    def __init__(self, *args, **kwargs):
        super(Driver, self).__init__(*args, **kwargs)
        self.handlers = {}


def create_driver(profile_path):
    if profile_path is None:
        profile = None
    else:
        profile = selenium.webdriver.FirefoxProfile(profile_path)
    driver = Driver(firefox_profile=profile, timeout=600)
    current_handler = driver.window_handles[-1]
    return driver, current_handler

def create_new_window(driver):
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 'n')
    current_handler = driver.window_handles[-1]
    return current_handler


class Webdriver(object):

    def __init__(self, profilepath=None, downloader=None):
        self.id = id(self)
        self.profilepath = None
        self.driver_regs = {}
        if downloader is not None:
            self.lock = downloader.lock
            self.driver_regs[self.id] = downloader.driver_regs[downloader.id]
            driver = downloader.driver_regs[downloader.id]['driver']
            handler = create_new_window(driver)
        else:
            self.lock = threading.Lock()
            self.profilepath = profilepath
            driver, handler = create_driver(self.profilepath)
            self.driver_regs[self.id] = {'driver': driver}
        driver.handlers[self.id] = handler
        self.driver.implicitly_wait(10)

    @property
    def driver(self):
        return self.driver_regs[self.id]['driver']

    def is_setup(self):
        self.driver.switch_to_window(self.driver.handlers[self.id])
        return self.driver.current_url != u'about:blank'

    def reset_driver(self):
        if self.profilepath is None:
            return
        ids = list(self.driver.handlers.keys())
        self.driver.quit()
        driver, handler = create_driver(self.profilepath)
        self.driver_regs[self.id]['driver'] = driver
        for _id in ids:
            if _id == self.id:
                _handler = handler
            else:
                _handler = create_new_window(self.driver)
            self.driver.handlers[_id] = _handler

    def switch_profile(self, profile_paths):
        if self.profilepath is None:
            return
        if self.profilepath in profile_paths:
            index = profile_paths.index(self.profilepath)
            next_index = (index + 1)%len(profile_paths)
            self.profilepath = profile_paths[next_index]
        else:
            self.profilepath = profile_paths[0]
        with self.lock:
            self.reset_driver()

    def getsource(self, url, form=None):
        page = ''
        with self.lock:
            try:
                self.driver.switch_to_window(self.driver.handlers[self.id])
            except socket.error:
                self.reset_driver()
                self.driver.switch_to_window(self.driver.handlers[self.id])
            if form is None:
                self.driver.get(url)
                page = self.driver.page_source
            else:
                page = self.post(url, form)
        return page

    def post(self, url, form):
        js = """function post(path, params) {
                    var xhr = new XMLHttpRequest();
                    xhr.open("POST", path, false);
                    var formData = new FormData();
                    for(var key in params) {
                        formData.append(key, params[key]);
                    }
                    xhr.send(formData);
                    var result = "";
                    if (xhr.readyState == 4) {
                        if (xhr.status == 200) {
                            result = xhr.responseText;
                        }
                    }

                    return result
                }
                url = %s;
                form = %s;

                return post(url, form);"""

        _url = '"' + url + '"'
        page = self.driver.execute_script(js%(_url, str(form)))
        return page

    def close(self):
        self.driver.quit()
