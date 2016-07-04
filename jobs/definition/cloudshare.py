import time

import storage.cv
import storage.jobtitles
import storage.fsinterface
import downloader.webdriver
import jobs.definition.base


class Cloudshare(jobs.definition.base.Base):

    def __init__(self):
        self.wb_downloader = downloader.webdriver.Webdriver(self.FF_PROFILE_PATH)
        self.precedure = self.PRECEDURE_CLASS(wbdownloader=self.wb_downloader)
        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)

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
            'tag': [],
            'tracking': [],
            }
        return template

    def extract_details(self, uploaded_details):
        details = self.cloudshare_yaml_template()
        details['date'] = uploaded_details['date']
        details['id'] = uploaded_details['id']
        details['originid'] = uploaded_details['id']
        details['filename'] = uploaded_details['href']
        return details