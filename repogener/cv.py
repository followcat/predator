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

    def add(self, cvobj, committer=None):
        shutil.copy(os.path.join(cvobj.markdown_path, cvobj.mdname),
                    os.path.join(self.repo_path, cvobj.mdname))
        cvobj.yamlinfo['committer'] = committer
        utils.builtin.save_yaml(cvobj.yamlinfo,
                                self.repo_path, cvobj.yamlname)
        self.repo.add_files([
                       os.path.join(self.repo_path, cvobj.mdname),
                       os.path.join(self.repo_path, cvobj.yamlname)],
                       committer=committer)
        return True

    def search(self, keyword):
        results = self.repo.grep(keyword, self.path)
        return results

    def search_yaml(self, keyword):
        results = self.repo.grep_yaml(keyword, self.path)
        return results
