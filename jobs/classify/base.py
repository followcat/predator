import utils.builtin
import storage.jobtitles
import downloader._urllib
import downloader.webdriver


class Base(object):

    ff_profile = None
    cookies_file = None

    def __init__(self, interface):
        if self.cookies_file is not None:
            self.cookies_str = utils.builtin.loadfile('cookies.data')
            self.downloader = downloader._urllib.Urllib()
            self.downloader.set_cookies(self.cookies_str)
        elif ff_profile is not None:
            self.downloader = downloader.webdriver.Webdriver(self.ff_profile)
        self.repojt = storage.jobtitles.JobTitles(interface)

    def jobgenerator(self):
        pass
