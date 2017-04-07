import utils.builtin
import downloader.webdriver


class Base(object):
    source = 'Base'

    def get_wb_downloader(self, profile_path, wbdownloaders=None):
        if isinstance(wbdownloaders, dict) and self.source in wbdownloaders:
            wbdownloader = wbdownloaders[self.source]
            return downloader.webdriver.Webdriver(downloader=wbdownloader)
        return downloader.webdriver.Webdriver(profile_path)

    def get_setting(self, config):
        settings = {}
        path = config[:config.rindex('/')]
        cfile = config[config.rindex('/')+1:]
        contents = utils.builtin.load_yaml(path, cfile)
        for k, v in contents.items():
            ind_file = v['industries']
            kw_file = v['keywords']
            inds = []
            kws = []
            with open(ind_file) as ind_f:
                for l in ind_f.readlines():
                    l = l.strip()
                    if l.startswith('#'):
                        continue
                    inds.append(l)
            with open(kw_file) as kw_f:
                for kw in kw_f.readlines():
                    if l.startswith("#"):
                        continue
                    kws.append(l.decode('utf-8'))
            settings[k] = (inds, kws)
        return settings
