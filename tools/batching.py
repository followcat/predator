import os

import utils.builtin

from sources.industry_id import *


def convert_rawhtml_from_repojt(instance):
    repojt = instance.repojt
    filenames = repojt.interface.lsfiles('JOBTITLES', '*.yaml')
    for filename in filenames:
        id = filename.replace('.yaml', '')
        info = repojt.get(id)
        if 'datas' in info:
            info = info['datas']
        for key in info:
            value = info[key]
            try:
                htmlraw = value.pop('html')
                with open(os.path.join(repojt.interface_path, repojt.yaml_raw_path,
                                       value['id']+'.html'), 'w') as f:
                    f.write(htmlraw.encode('utf-8'))
            except KeyError:
                continue
        repojt.modify_data(id, info, 'BATCHING', 'Convert %s raw html from yaml to files.' % id)


def add_tags_to_cv_raw_yaml(industries, instance, jb_path, cv_raw_path):
    for industry in industries:
        _classify_id = industryID[industry.encode('utf-8')]
        _file = _classify_id + '.yaml'
        try:
            yamlfile = utils.builtin.load_yaml(jb_path, _file)
            yamldata = yamlfile['datas']
        except Exception:
            continue
        for cv_id in yamldata.keys():
            try:
                yamlload = utils.builtin.load_yaml(cv_raw_path, cv_id+'.yaml')
            except IOError:
                continue
            try:
                yamlload.pop('tag')
            except KeyError:
                pass
            yamlload['tags'] = yamldata[cv_id]['tags']
            resultpath = instance.cvstorage.addyaml(cv_id, yamlload)
