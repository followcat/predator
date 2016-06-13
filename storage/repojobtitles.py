import glob
import yaml
import utils._yaml
import os.path

import utils.builtin


class JobTitles(object):
    path = 'JOBTITLES'

    def __init__(self, repo):
        self.repo = repo
        self.repo_path = self.repo.repo.path + "/" + self.path
        self.info = ""
        self.table = {}
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)

    def add_datas(self, classify_id, datas, committer):
        filename = classify_id + '.yaml'
        file_path = os.path.join(self.repo_path, filename)

        self._initclassify(classify_id)
        table = utils.builtin.load_yaml(self.repo_path, filename)

        for data in datas:
            table[data['id']] = data
        dump_data = yaml.safe_dump(table, allow_unicode=True)
        self.repo.modify_file(os.path.join(self.path, filename), dump_data,
                              message="Add to classify id :" + filename,
                              committer=committer)
        return True

    def exists(self, classify_id, data_id):
        if classify_id not in self.table:
            self._initclassify(classify_id)
            self.table[classify_id] = utils.builtin.load_yaml(self.repo_path, classify_id+'.yaml')
        exists = False
        if data_id in self.table[classify_id]:
            exists = True
        return exists

    def _initclassify(self, classify_id):
        filename = classify_id + '.yaml'
        file_path = os.path.join(self.repo_path, filename)
        if not os.path.exists(file_path):
            table = {}
            with open(file_path, 'w') as f:
                f.write(yaml.safe_dump(table, allow_unicode=True))
            self.repo.add_files(os.path.join(self.path, filename),
                                "Add classify file: " + filename)

