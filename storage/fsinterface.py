import glob
import os.path


class FSInterface(object):

    def __init__(self, path):
        self.path = path

    def lsfiles(self, prefix, filterfile):
        return [os.path.split(f)[1] for f in glob.glob(
                os.path.join(self.path, prefix, filterfile))]

    def add_file(self, filename, filedate, *args, **kwargs):
        file_path = os.path.join(self.path, filename)
        with open(file_path, 'w') as f:
            f.write(filedate)
        return True

    def modify_file(self, filename, filedate, *args, **kwargs):
        file_path = os.path.join(self.path, filename)
        with open(file_path, 'w') as f:
            f.write(filedate)
        return True
