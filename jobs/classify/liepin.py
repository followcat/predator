import utils.builtin
import precedure.liepin
import downloader._urllib
import storage.jobtitles
import storage.gitinterface
from sources.liepin import localdatajobs


cookies_str = utils.builtin.loadfile('cookies.data')
ul_downloader = downloader._urllib.Urllib()
ul_downloader.set_cookies(cookies_str)
liepin = precedure.liepin.Liepin(uldownloader=ul_downloader)

repo = storage.gitinterface.GitInterface('liepin')
repojt = storage.jobtitles.JobTitles(repo)
selected_list = [
'290094', #医疗器械研发
'290097', #医疗器械生产/质量管理
'060010', #市场总监
'020010', #销售总监
'040020', #项目经理/主管
'040040', #项目专员/助理
'050010', #质量管理/测试经理(QA/QC经理)
'050080', #体系工程师/审核员
'050020', #质量管理/测试主管(QA/QC主管)
]
for id_str in selected_list:
    print localdatajobs['jobtitles'][id_str][0]
    postdict = {'industrys': 290,
                'jobtitles': id_str,
                'curPage': 0}
    liepin.update_classify(postdict, repojt)
