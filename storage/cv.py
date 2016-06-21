import os.path


class CurriculumVitae(object):

    path = 'CV'
    extension = '.html'

    def __init__(self, interface):
        self.interface = interface
        self.interface_path = self.interface.path + "/" + self.path
        self.info = ""
        self.table = {}
        if not os.path.exists(self.interface_path):
            os.makedirs(self.interface_path)

    def add(self, cv_id, data, committer=None, unique=True):
        if unique and self.exists(cv_id):
            return False
        filename = cv_id + self.extension
        self.interface.add_file(os.path.join(self.path, filename),
                                data,
                                "Add cv file: " + filename,
                                committer=committer)
        return True

    def exists(self, cv_id):
        exists = False
        filename = cv_id + self.extension
        file_path = os.path.join(self.interface_path, filename)
        if os.path.exists(file_path):
            exists = True
        return exists

    def get(self, cv_id):
        data = None
        if self.exists(cv_id):
            filename = cv_id + self.extension
            with open(filename) as fp:
                data = fp.read()
        return data
