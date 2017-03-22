import downloader.webdriver


class Base(object):
    source = 'Base'

    def get_wb_downloader(self, profile_path, wbdownloaders=None):
        if isinstance(wbdownloaders, dict) and self.source in wbdownloaders:
            wbdownloader = wbdownloaders[self.source]
            return downloader.webdriver.Webdriver(downloader=wbdownloader)
        return downloader.webdriver.Webdriver(profile_path)



