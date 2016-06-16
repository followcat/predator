import utils.builtin
import precedure.liepin


CVDB_PATH = 'liepin_webdrivercv'
FF_PROFILE_PATH = '/home/followcat/.mozilla/firefox/yffp11op.followcat'
PRECEDURE_CLASS = precedure.liepin.Liepin
YAMLDATA = utils.builtin.load_yaml('liepin/JOBTITLES', '290097.yaml')

PLAN = [dict(minute='*/1', hour='8-17'),
        dict(minute='*/15', hour='18-23'),
        dict(minute='*/15', hour='0-2')]