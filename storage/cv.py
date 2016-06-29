import yaml
import os.path
import pypandoc


class CurriculumVitae(object):

    mdpath = 'CV'
    mdextension = '.md'
    yamlpath = 'CV'
    yamlextension = '.yaml'
    rawpath = 'RAW'
    rawextension = '.html'

    def __init__(self, interface):
        self.interface = interface
        self.interface_path = self.interface.path + "/" + self.mdpath
        self.interface_rawpath = self.interface.path + "/" + self.rawpath
        self.info = ""
        self.table = {}
        if not os.path.exists(self.interface_path):
            os.makedirs(self.interface_path)
        if not os.path.exists(self.interface_rawpath):
            os.makedirs(self.interface_rawpath)

    def addcv(self, cv_id, data, yamldata, committer=None, unique=True):
        rawpath = self.addraw(cv_id, data, committer)
        md = pypandoc.convert(data, 'markdown', format='docbook')
        self.addmd(cv_id, md.encode('utf-8'), committer)
        self.addyaml(cv_id, yamldata, committer)
        return True

    def add(self, cv_id, data, committer=None, unique=True):
        if unique and self.exists(cv_id):
            return False
        filename = cv_id + self.rawextension
        filepath = os.path.join(self.mdpath, filename)
        self._add(filepath, filename, data, committer)
        return True

    def _add(self, path, filename, data, committer):
        self.interface.add_file(path, data, "Add cv file: " + filename,
                                committer=committer)

    def addmd(self, cv_id, data, committer=None, unique=True):
        filename = cv_id + self.mdextension
        filepath = os.path.join(self.mdpath, filename)
        self._add(filepath, filename, data, committer)
        return filepath

    def addyaml(self, cv_id, data, committer=None, unique=True):
        filename = cv_id + self.yamlextension
        filepath = os.path.join(self.yamlpath, filename)
        dump_data = yaml.safe_dump(data, allow_unicode=True)
        self._add(filepath, filename, dump_data, committer)
        return filepath

    def addraw(self, cv_id, data, committer=None, unique=True):
        filename = cv_id + self.rawextension
        filepath = os.path.join(self.rawpath, filename)
        self._add(filepath, filename, data, committer)
        return filepath

    def exists(self, cv_id):
        exists = False
        filename = cv_id + self.rawextension
        file_path = os.path.join(self.interface_path, filename)
        if os.path.exists(file_path):
            exists = True
        return exists

    def existscv(self, cv_id):
        result = False
        if (self.existsyaml(cv_id) and
            self.existsmd(cv_id) and
            self.existsraw(cv_id)):
            result = True
        return result

    def existsmd(self, cv_id):
        exists = False
        filename = cv_id + self.mdextension
        file_path = os.path.join(self.interface_path, filename)
        if os.path.exists(file_path):
            exists = True
        return exists

    def existsyaml(self, cv_id):
        exists = False
        filename = cv_id + self.yamlextension
        file_path = os.path.join(self.interface_path, filename)
        if os.path.exists(file_path):
            exists = True
        return exists

    def existsraw(self, cv_id):
        exists = False
        filename = cv_id + self.rawextension
        file_path = os.path.join(self.interface_rawpath, filename)
        if os.path.exists(file_path):
            exists = True
        return exists

    def get(self, cv_id):
        data = None
        if self.exists(cv_id):
            filename = os.path.join(self.interface_path, cv_id) + self.rawextension
            data = self._get(filename)
        return data

    def _get(self, path):
        with open(path) as fp:
            data = fp.read()
        return data

    def getmd(self, cv_id):
        data = None
        if self.existsmd(cv_id):
            filename = os.path.join(self.interface_path, cv_id) + self.mdextension
            data = self._get(filename)
        return data

    def getyaml(self, cv_id):
        data = None
        if self.existsyaml(cv_id):
            filename = os.path.join(self.interface_path, cv_id) + self.yamlextension
            data = self._get(filename)
        return data

    def getraw(self, cv_id):
        data = None
        if self.existsraw(cv_id):
            filename = os.path.join(self.interface_rawpath, cv_id) + self.rawextension
            data = self._get(filename)
        return data
