import os.path


class FSInterface(object):

    def __init__(self, path):
        self.path = path

    def add_file(self, filename, **kwargs):
        file_path = os.path.join(self.path, filename)
        with open(file_path, 'w') as f:
            f.write(data)
        return True

    def modify_file(self, filename, stream, **kwargs):
        with open(os.path.join(self.path, filename), 'w') as f:
            f.write(stream)
        return True
