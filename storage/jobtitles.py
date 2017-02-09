import glob
import yaml
import os.path
import utils._yaml

import utils.builtin


class JobTitles(object):
    path = 'JOBTITLES'
    yaml_raw_path = 'HTMLRAW'

    def __init__(self, interface):
        self.interface = interface
        self.interface_path = os.path.join(self.interface.path, self.path)
        self.interface_rawpath = os.path.join(self.interface.path, self.path, self.yaml_raw_path)
        self.info = ""
        self.table = {}
        if not os.path.exists(self.interface_path):
            os.makedirs(self.interface_path)
        if not os.path.exists(self.interface_rawpath):
            os.makedirs(self.interface_rawpath)

    def get(self, classify_id):
        if classify_id not in self.table:
            yamlname = classify_id + '.yaml'
            if not os.path.exists(os.path.join(self.interface_path, yamlname)):
                return None
            yamldata = utils.builtin.load_yaml(self.interface_path, yamlname)
            self.table[classify_id] = yamldata
        return self.table[classify_id]

    def getraw(self, id):
        with open(os.path.join(self.interface_rawpath, id+'.html')) as fp:
            stream = fp.read()
        return stream

    def unload(self, classify_id):
        result = False
        if classify_id in self.table:
            self.table.pop(classify_id)
            result = True
        return result

    def remove(self, classify_id, cv_id):
        yamldata = self.get(classify_id)
        removed = yamldata.pop(cv_id)
        self.modify_data(classify_id, yamldata)
        return removed

    def add_datas(self, classify_id, datas, update_datas, header, committer=None):
        if len(datas) == 0 and len(update_datas) == 0:
            return True
        if header is None:
            header = dict()
        filename = classify_id + '.yaml'
        table = self.get(classify_id)

        rawhtml = dict()
        for data in datas+update_datas:
            htmlraw = data.pop('html')
            self.interface.add_file(os.path.join(self.interface_rawpath, data['id']+'.html'),
                                    htmlraw, message="Add to raw html id :" + filename,
                                    committer=committer)

        if 'datas' not in table:
            new_table = dict()
            new_table['datas'] = dict()
            new_table['datas'].update(table)
            table = new_table
        table.update(header)
        for data in datas:
            table['datas'][data['id']] = data

        if update_datas is not None:
            for data in update_datas:
                if data['id'] not in table['datas']:
                    table['datas'][data['id']] = data
                    continue
                current = table['datas'][data['id']]
                for key in data['tags'].keys():
                    if key not in current['tags']:
                        current['tags'][key] = set()
                    current['tags'][key] = current['tags'][key].union(data['tags'][key])

        dump_data = yaml.dump(table, Dumper=yaml.CSafeDumper, allow_unicode=True)
        self.interface.add_file(os.path.join(self.path, filename), dump_data,
                                message="Add to classify id :" + filename,
                                committer=committer)
        return True

    def modify_data(self, classify_id, data, committer=None, message=None):
        filename = classify_id + '.yaml'
        dump_data = yaml.dump(data, Dumper=yaml.CSafeDumper, allow_unicode=True)
        self.interface.modify_file(os.path.join(self.path, filename), dump_data,
                                   message=message, committer=committer)
        self.table[classify_id] = data
        return True

    def exists(self, classify_id, data_id):
        if classify_id not in self.table:
            self._initclassify(classify_id)
            self.table[classify_id] = utils.builtin.load_yaml(self.interface_path, classify_id+'.yaml')
        exists = False
        if 'datas' in self.table[classify_id]:
            datas = self.table[classify_id]['datas']
        else:
            datas = self.table[classify_id]
        return data_id in datas

    def _initclassify(self, classify_id):
        filename = classify_id + '.yaml'
        file_path = os.path.join(self.interface_path, filename)
        if not os.path.exists(file_path):
            table = {}
            self.interface.add_file(os.path.join(self.path, filename),
                                    yaml.dump(table, Dumper=yaml.CSafeDumper, allow_unicode=True),
                                    "Add classify file: " + filename)

    def lenght(self, classify_id):
        result = None
        info = self.get(classify_id)
        if info is not None:
            result = len(info['datas'])
        return result
