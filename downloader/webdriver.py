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
        with self.lock:
            try:
                self.driver.switch_to_window(self.driver.handlers[self.id])
                if form is None:
                    self.driver.get(url)
                else:
                    self.post(url, form)
            except socket.error:
                self.reset_driver()
                self.driver.switch_to_window(self.driver.handlers[self.id])
                if form is None:
                    self.driver.get(url)
                else:
                    self.post(url, form)
            page = self.driver.page_source
        return page

    def post(self, url, form):
        js = """function post(path, params, method) {
                    method = method || "post"; // Set method to post by default if not specified.
                    var form = document.createElement("form");
                    form.setAttribute("method", method);
                    form.setAttribute("action", path);

                    for(var key in params) {
                        if(params.hasOwnProperty(key)) {
                            var hiddenField = document.createElement("input");
                            hiddenField.setAttribute("type", "hidden");
                            hiddenField.setAttribute("name", key);
                            hiddenField.setAttribute("value", params[key]);

                            form.appendChild(hiddenField);
                         }
                    }

                    document.body.appendChild(form);
                    form.submit();
                }

                form = %s;
                url = %s;

                post(url, form);"""

        _url = '"' + url + '"'
        self.driver.execute_script(js%(str(form), _url))

    def close(self):
        self.driver.quit()
