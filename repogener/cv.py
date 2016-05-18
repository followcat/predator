import time
import shutil
import os.path

import utils.builtin


class RepoCurriculumVitae(object):

    path = 'CV'

    def __init__(self, repo):
        self.repo = repo
        self.repo_path = self.repo.repo.path + "/" + self.path
        self.info = ""
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)

    def add(self, files, committer=None):                                       
        self.repo.add_files(files, committer=committer) 

    def search(self, keyword):
        results = self.repo.grep(keyword, self.path)
        return results

    def search_yaml(self, keyword):
        results = self.repo.grep_yaml(keyword, self.path)
        return results
