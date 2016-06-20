class FSInterface(object):

    def __init__(self, path):
        self.path = path

    def add_files(self, filenames, **kwargs):
        pass

    def modify_file(self, filename, stream, **kwargs):
        pass
