import utils.builtin
import precedure.jingying
import downloader._urllib
import storage.jobtitles
import storage.fsinterface

from sources.jingying import *


cookies_str = utils.builtin.loadfile('cookies.data').rstrip('\n')
ul_downloader = downloader._urllib.Urllib()
ul_downloader.set_cookies(cookies_str)
repo = storage.fsinterface.FSInterface('jingying')
repojt = storage.jobtitles.JobTitles(repo)
jingying = precedure.jingying.Jingying(uldownloader=ul_downloader)
#start from industry
industry_list = [
'47', #医疗设备/器械
'01', #计算机软件
'37', #计算机硬件
'38', #计算机服务(系统、数据服务、维修)
'31', #通信/电信/网络设备
'35', #仪器仪表/工业自动化
'14', #机械/设备/重工
'52', #检测，认证
'07', #专业服务(咨询、人力资源、财会)
'24', #学术/科研
'21', #交通/运输/物流
'55', #航天/航空
'36', #电气/电力/水利
'55', #航天/航空
'61', #新能源
]
for id_str in industry_list:
    print localdatajobs['industry'][id_str]
    postdict = {'indtype': id_str,
                'curr_page': '0'}
    jingying.update_classify(id_str, postdict, repojt)

#Then go on with company names group by area
company_area_list = [
    'GuangDong',        #广东
    'ShangHai',         #上海
    'JiangSu',          #江苏
    'BeiJing',          #北京
    'ZheJiang',         #浙江
    'HuNan',            #湖南
    'AnHui',            #安徽
    'JiangXi',          #江西
    'GuangXi',          #广西
    'SiChuan',          #四川
    'NorthEast',        #东北
    'ShanDong',         #山东
    'TianJin',          #天津
    'ShanXi(Shan)',     #陕西（陕）
    'ShanXi(Jin)',      #山西（晋）
    'HeBei',            #河北
    'HuBei',            #湖北
    'FuJian',           #福建
    'Others',           #其他
    ]
for _area in company_area_list:
    for c_name in localdatajobs['company_name'][_area]:
        print c_name
        postdict = {'cotext': c_name.decode('utf-8').encode('gb2312'),
                    'curr_page': '0'}
        jingying.update_classify(_area, postdict, repojt)
