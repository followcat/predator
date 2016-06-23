class NotImplementedInterface(Exception):
    pass


class Base(object):
    
    def __init__(self):
        pass

    def urlget_classify(self):
        raise NotImplementedInterface

    def urlget_cv(self):
        raise NotImplementedInterface

    def webdriverget_classify(self):
        raise NotImplementedInterface

    def webdriverget_cv(self):
        raise NotImplementedInterface

    def parse_classify(self):
        raise NotImplementedInterface

    def parse_cv(self):
        raise NotImplementedInterface

    def classify(self):
        raise NotImplementedInterface

    def cv(self):
        raise NotImplementedInterface
