import os


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
            htmlraw = value.pop('html')
            with open(os.path.join(repojt.interface_path, repojt.yaml_raw_path,
                                   value['id']+'.html'), 'w') as f:
                f.write(htmlraw.encode('utf-8'))
        repojt.modify_data(id, info, 'BATCHING', 'Convert %s raw html from yaml to files.' % id)
