import utils.builtin
import storage.jobtitles
import downloader._urllib
import downloader.webdriver
import sources.mapping.tags

class Base(object):

    ff_profile = None
    cookies_file = None
    precedure = None
    precedure_type = None
    wbdownloader = False
    uldownloader = False


    def __init__(self, interface):
        if self.cookies_file is not None:
            self.cookies_str = utils.builtin.loadfile('cookies.data').strip()
            self.downloader = downloader._urllib.Urllib()
            self.downloader.set_cookies(self.cookies_str)
        elif self.ff_profile is not None:
            self.downloader = self.get_wb_downloader(self.ff_profile)
        self.repojt = storage.jobtitles.JobTitles(interface)
        self.precedure = self.get_precedure()

    def get_precedure(self):
        precedure = None
        if self.precedure is None and self.precedure_type is not None:
            if self.uldownloader is True:
                precedure = self.precedure_type(uldownloader=self.downloader)
            elif self.wbdownloader is True:
                precedure = self.precedure_type(wbdownloader=self.downloader)
        else:
            precedure = self.precedure
        return precedure

    def get_wb_downloader(self,profile_path):
        return downloader.webdriver.Webdriver(profile_path)

    def industryjob(self, industryid, filename, industry, resume=False):
        pass

    def jobgenerator(self):
        pass

    def get_postdict(self, classifyid):
        result = dict()
        data = self.repojt.get(classifyid)
        if 'postdict' in data:
            result = data['postdict']
        return result

    def eq_postdict(self, classifyid, postdict, exclude=None):
        if exclude is None:
            exclude = []

        last_head = self.get_postdict(classifyid)
        for p in postdict:
            if p in exclude:
                continue
            if p in last_head and postdict[p] == last_head[p]:
                continue
            else:
                return False
        for p in last_head:
            if p in exclude:
                continue
            if p in postdict and postdict[p] == last_head[p]:
                continue
            else:
                return False
        return True

    def gen_header(self, postdict, postinfo):
        for _k, _v in postinfo.items():
            if not isinstance(_v, unicode):
                postinfo[_k] = _v.decode('utf-8')
        header = {
            'tags' :  postinfo,
            'postdict': postdict.copy(),
        }
        return header
