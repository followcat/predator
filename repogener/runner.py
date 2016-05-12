# -*- coding: utf-8 -*-

import time
import path
import yaml
import os.path
import regex as re

import pypandoc

def cloudshare_yaml_template():
    template = {
        'age': 99,
        'comment': [],
        'committer': "SCRAPPY",
        'company': "",
        'date': 0.,
        'education': "",
        'email': 'norepply@example.com',
        'experience': [],
        'filename': "",
        'id': '',
        'name': "",
        'origin': '',
        'phone': "",
        'position': "",
        'school': "",
        'tag': [],
        'tracking': [],
        }
    return template


def extract_details(uploaded_details):
    DATE = '(([0-9]{4,4}[\./][0-9]{2,2})|(\\\\u81F3\\\\u4ECA))'
    WORKXP = ur"(\d{4}[/.\\年 ]+\d{1,2}[月]*)[-– —]*(\d{4}[/.\\年 ]+\d{1,2}[月]*|至今)[：: ]*([^\n,，.。（（:]*)"
    STUDIES = u'\s*'+DATE+' - '+DATE+'(?P<expe>[^\(].+?)(?='+DATE+'|$)'

    details = cloudshare_yaml_template()

    details['date'] = time.time()
    details['id'] = uploaded_details['id']
    details['company'] = uploaded_details['peo'][7]
    details['position'] = uploaded_details['peo'][6]
    details['filename'] = uploaded_details['href']
    details['age']= re.compile('[0-9]*').match(uploaded_details['peo'][2]).group()
    try:
        education = re.compile(STUDIES, re.M).search(uploaded_details['info'][0]).group('expe')
    except:
        education = ''
    details['school'] = education.split('|')[0]
    details['education'] = education.split('|')[-1]
    for expe in uploaded_details['info']:
        work = re.compile(WORKXP).findall(expe)
        for w in work:
            details['experience'].append(list(w))
    return details


import interface.repocv
import interface.gitinterface
import repogener.cv

if __name__ == '__main__':
    with open('liepin/JOBTITLES/290094.yaml') as f:
        text = f.read()
    inputrepo = interface.gitinterface.GitInterface('liepin_cv')
    inputcv = interface.repocv.CurriculumVitae(inputrepo)

    outputrepo = interface.gitinterface.GitInterface('liepinrepo')
    outputcv = repogener.cv.RepoCurriculumVitae(outputrepo)
    res = yaml.load(text)
    for id_str in res:
        if inputcv.exists(id_str):
            filename = os.path.join(inputcv.repo_path, id_str+inputcv.extension)
            output = pypandoc.convert(filename, 'markdown_github', format='html')
            out = os.path.join(outputcv.repo_path, id_str)
            with open(out+'.md', 'w') as _f:
                for line in output.split('\n'):
                    data = line.lstrip(' ')+'\n'
                    _f.write(data.encode('utf-8'))
            uploaded_details = res[id_str]
            with open(out+'.yaml', 'w') as f:
                f.write(yaml.dump(extract_details(uploaded_details)).encode('utf8'))
