# -*- coding: utf-8 -*-
import yaml
import os
import utils.builtin

from sources.industry_id import*
cvpath = 'output/yingcai/RAW/'
cvlistpath = 'yingcai/JOBTITLES'

def add_file(path, filename, filedate):
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as f:
        f.write(filedate)
    return True

def existscv(path, cv_id):
    exists = False
    filename = cv_id + '.yaml'
    file_path = os.path.join(path, filename)
    if os.path.exists(file_path):
        exists = True
    return exists

for _classify_id in industryID.values():
    print _classify_id
    _file = _classify_id + '.yaml'
    try:
      yamlfile = utils.builtin.load_yaml(cvlistpath, _file)
      yamldata = yamlfile['datas']
    except IOError:
        continue
    sorted_id = sorted(yamldata,
                       key = lambda cvid: yamldata[cvid]['info'][-1],
                       reverse=True)
    for cv_id in sorted_id:
        if not existscv(cvpath, cv_id):
            continue
        else:
            print cv_id
            try:
                cvdata = utils.builtin.load_yaml(cvpath, cv_id+'.yaml')
            except Exception:
                print "Load error :",cv_id
                continue
            try:
                yamldata.pop('tag')
            except KeyError:
                pass
            if 'tags' in cvdata.keys() and len(cvdata['tags'].keys())!=0:
                continue
            else:
                cvdata['tags'] = {}
                cvdata['tags'] = yamldata[cv_id]['tags']
            dump_data = yaml.dump(cvdata, Dumper=yaml.CSafeDumper, allow_unicode=True)
            add_file(cvpath, cv_id+'.yaml', dump_data)
