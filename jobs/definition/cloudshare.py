import time

import storage.cv
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

    def jobgenerator(self, industry_needed, keywords=None):
        try:
            while True:
                for job in self.simple_jobgenerator(industry_needed, keywords):
                    yield job
        except:
            return

    def simple_jobgenerator(self, industry_needed, keywords=None):
        pass
