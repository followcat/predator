import glob
import yaml
import utils._yaml
import os.path

import utils.builtin


class JobTitles(object):
    path = 'JOBTITLES'

    def __init__(self, interface):
        self.interface = interface
        self.interface_path = self.interface.path + "/" + self.path
        self.info = ""
        self.table = {}
        if not os.path.exists(self.interface_path):
            os.makedirs(self.interface_path)

    def get(self, classify_id):
        yamlname = classify_id + '.yaml'
        yamldata = utils.builtin.load_yaml(self.interface_path, yamlname)
        return yamldata

    def add_datas(self, classify_id, datas, committer=None):
        filename = classify_id + '.yaml'
        file_path = os.path.join(self.interface_path, filename)

        self._initclassify(classify_id)
        table = utils.builtin.load_yaml(self.interface_path, filename)

        for data in datas:
            table[data['id']] = data
        dump_data = yaml.safe_dump(table, allow_unicode=True)
        self.interface.add_file(os.path.join(self.path, filename), dump_data,
                                message="Add to classify id :" + filename,
                                committer=committer)
        return True

    def add_data(self, classify_id, data, committer=None):
        filename = classify_id + '.yaml'
        dump_data = yaml.dump(data, Dumper=yaml.CSafeDumper, allow_unicode=True)
        self.interface.add_file(os.path.join(self.path, filename), dump_data,
                                message="Add to classify id :" + filename,
                                committer=committer)
        return True

    def modify_data(self, classify_id, data, committer=None):
        filename = classify_id + '.yaml'
        dump_data = yaml.dump(data, Dumper=yaml.CSafeDumper, allow_unicode=True)
        self.interface.modify_file(os.path.join(self.path, filename), dump_data,
                                   message="Add to classify id :" + filename,
                                   committer=committer)
        return True

    def exists(self, classify_id, data_id):
        if classify_id not in self.table:
            self._initclassify(classify_id)
            self.table[classify_id] = utils.builtin.load_yaml(self.interface_path, classify_id+'.yaml')
        exists = False
        if data_id in self.table[classify_id]:
            exists = True
        return exists

    def _initclassify(self, classify_id):
        filename = classify_id + '.yaml'
        file_path = os.path.join(self.interface_path, filename)
        if not os.path.exists(file_path):
            table = {}
            self.interface.add_file(os.path.join(self.path, filename),
                                    yaml.safe_dump(table, allow_unicode=True),
                                    "Add classify file: " + filename)

