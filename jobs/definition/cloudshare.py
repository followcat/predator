import time

import storage.cv
import utils.builtin
import storage.jobtitles
import storage.fsinterface
import downloader.webdriver
import jobs.definition.base


class Cloudshare(jobs.definition.base.Base):

    def __init__(self, wbdownloaders=None):
        self.wb_downloader = self.get_wb_downloader(self.FF_PROFILE_PATH, wbdownloaders)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtrepo = storage.gitinterface.GitInterface(self.JTDB_PATH)
        self.jtstorage = storage.jobtitles.JobTitles(self.jtrepo)

    def cloudshare_yaml_template(self):
        template = {
            'age': 0,
            'comment': [],
            'committer': "SCRAPPY",
            'company': "",
            'date': 0.,
            'education': "",
            'email': "",
            'experience': [],
            'filename': "",
            'id': "",
            'originid': "",
            'name': "",
            'origin': "",
            'phone': "",
            'position': "",
            'school': "",
            'tags': {},
            'tracking': [],
            }
        return template

    def extract_details(self, uploaded_details):
        details = self.cloudshare_yaml_template()
        details['date'] = time.time()
        details['id'] = uploaded_details['id']
        details['originid'] = uploaded_details['id']
        details['filename'] = uploaded_details['href']
        return details

    def get_cv_list(self, file_name, keywords):
        yamlfile = utils.builtin.load_yaml('output/%s/JOBTITLES'%self.source, file_name)
        _tmpdata = yamlfile['datas']
        if keywords is None or len(keywords) == 0:
            yamldata = _tmpdata
        else:
            yamldata = {}
            for _k, _v in _tmpdata.items():
                if 'searchtext' in _v['tags']:
                    for keyword in keywords:
                        if keyword in _v['tags']['searchtext']:
                            yamldata[_k] = _v
                            break
        return yamldata

    def jobgenerator(self, industry_needed, keywords=None):
        try:
            while True:
                for job in self.simple_jobgenerator(industry_needed, keywords):
                    yield job
        except:
            return

    def simple_jobgenerator(self, industry_needed, keywords=None):
        pass
