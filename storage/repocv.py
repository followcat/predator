import os.path


class CurriculumVitae(object):

    path = 'CV'
    extension = '.html'

    def __init__(self, repo):
        self.repo = repo
        self.repo_path = self.repo.repo.path + "/" + self.path
        self.info = ""
        self.table = {}
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)

    def add(self, cv_id, data, committer, unique=True):
        if unique and self.exists(cv_id):
            return False
        filename = cv_id + self.extension
        file_path = os.path.join(self.repo_path, filename)
        
        with open(file_path, 'w') as f:
            f.write(data)
        self.repo.add_files(os.path.join(self.path, filename),
                            "Add cv file: " + filename,
                            committer=committer)
        return True

    def exists(self, cv_id):
        exists = False
        filename = cv_id + self.extension
        file_path = os.path.join(self.repo_path, filename)
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
