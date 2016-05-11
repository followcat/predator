import glob
import os.path

import utils.builtin
import htmlparser.liepin
import downloader.liepin
import interface.repocv
import interface.gitinterface
import interface.repojobtitles


def update_title_cv(yamldata, cv):
    for cv_id in yamldata:
        if cv.exists(cv_id):
            continue
        cv_info = yamldata[cv_id]
        cv_url = cv_info['href']
        htmlsource = downloader.liepin.cv(cv_url)
        cv_content = htmlparser.liepin.catchcv(htmlsource)
        result = cv.add(cv_id, cv_content.encode('utf-8'), 'followcat')
        print cv_id

def update_all_cv(jt, cv):
    for pathfile in glob.glob(os.path.join(jt.repo_path, '*.yaml')):
        path, name = os.path.split(pathfile)
        yamldata = utils.builtin.load_yaml(path, name)
        update_title_cv(yamldata, cv)


if __name__ == '__main__':
    jtrepo = interface.gitinterface.GitInterface('liepin')
    jt = interface.repojobtitles.JobTitles(jtrepo)
    cvrepo = interface.gitinterface.GitInterface('liepin_cv')
    cv = interface.repocv.CurriculumVitae(cvrepo)
    update_all_cv(jt, cv)
