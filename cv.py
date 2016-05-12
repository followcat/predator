import glob
import os.path

import utils.builtin
import htmlparser.liepin
import downloader.liepin
import storage.repocv
import storage.gitinterface
import storage.repojobtitles


def update_title_cv(yamldata, cv):
    for cv_id in yamldata:
        if cv.exists(cv_id):
            continue
        htmlsource = downloader.liepin.cv(cv_id)
        cv_content = htmlparser.liepin.catchcv(htmlsource)
        result = cv.add(cv_id, cv_content.encode('utf-8'), 'followcat')
        print cv_id

def update_all_cv(jt, cv):
    for pathfile in glob.glob(os.path.join(jt.repo_path, '*.yaml')):
        path, name = os.path.split(pathfile)
        yamldata = utils.builtin.load_yaml(path, name)
        update_title_cv(yamldata, cv)


def update_select_cv(jt, cv, selected):
    for id_str in selected:
        path, name = jt.repo_path, id_str+'.yaml'
        yamldata = utils.builtin.load_yaml(path, name)
        update_title_cv(yamldata, cv)


if __name__ == '__main__':
    jtrepo = storage.gitinterface.GitInterface('liepin')
    jt = storage.repojobtitles.JobTitles(jtrepo)
    cvrepo = storage.gitinterface.GitInterface('liepin_cv')
    cv = storage.repocv.CurriculumVitae(cvrepo)
    update_all_cv(jt, cv)
