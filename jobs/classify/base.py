import utils.builtin
import storage.jobtitles
import downloader._urllib
import downloader.webdriver
import sources.mapping.tags

class Base(object):

    ff_profile = None
    cookies_file = None

    def __init__(self, interface):
        if self.cookies_file is not None:
            self.cookies_str = utils.builtin.loadfile('cookies.data')
            self.downloader = downloader._urllib.Urllib()
            self.downloader.set_cookies(self.cookies_str)
        elif self.ff_profile is not None:
            self.downloader = self.get_wb_downloader(self.ff_profile)
        self.repojt = storage.jobtitles.JobTitles(interface)

    def get_wb_downloader(self,profile_path):
        return downloader.webdriver.Webdriver(profile_path)

    def jobgenerator(self):
        pass

    def get_header(self, postdict, postinfo):
        header = {
            'tags' :  postinfo,
            'postdict': postdict
        }
        return header
