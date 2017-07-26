import os
import glob

import utils.builtin
import downloader.webdriver

from sources.industry_needed import industry_needed as default_industries


class Base(object):
    source = 'Base'

    def get_wb_downloader(self, profile_path, wbdownloaders=None):
        if isinstance(wbdownloaders, dict) and self.source in wbdownloaders:
            wbdownloader = wbdownloaders[self.source]
            return downloader.webdriver.Webdriver(downloader=wbdownloader)
        return downloader.webdriver.Webdriver(profile_path)

    def get_setting(self, config):
        settings = []
        if config != '':
            contents = utils.builtin.load_yaml('', config)
            for k, v in contents.items():
                kws = []
                inds = utils.builtin.load_yaml('', ind_file)
                ind_file = v['industries']
                if 'keywords' in v:
                    for _k, _v in utils.builtin.load_yaml('', v['keywords']).items():
                        kws.extend(_v)
                if 'keywordpath' in v:
                    for filepath in glob.glob(os.path.join(v['keywordpath'], '*.yaml')):
                        kpt_dict = utils.builtin.load_yaml(*os.path.split(filepath))
                        for pos in kpt_dict:
                            for keywords_list in pos.values():
                                for keywords in keywords_list:
                                    if len(keywords.split(' ')) < 7 and keywords:
                                        kws.append(keywords)
                settings.append((inds, kws))
        default_keywords = []
        settings.append((default_industries, default_keywords))
        return settings
