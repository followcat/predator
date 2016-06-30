import time

import bs4

import utils.tools
import htmlparser.tools

def source():
    html = ""
    with open("cv.txt") as fp:
        html = fp.read()
    return html


def catchman():
    htmlsource = source()
    bs = bs4.BeautifulSoup(htmlsource, 'lxml')
    data_lists = bs.findAll(class_='bor-bottom')
    result = []
    for index in range(1, len(data_lists), 2):
        storage_data = { 'peo': [], 'info': [] }
        storage_data['date'] = time.time()
        storage_data['recommend'] = ''
        storage_data['elite'] = ''
        storage_data['name'] = ''
        storage_data['data-name'] = ''
        storage_data['data-id'] = ''
        cur_situation = data_lists[index]
        abstract = data_lists[int(index+1)]
        storage_data['html'] = cur_situation.prettify() + abstract.prettify()
        peo_list = cur_situation.findAll(class_='list-three')
        for peo_item in peo_list:
            if peo_item.find("a") is not None:
                element_a = peo_item.find("a")
                storage_data['href'] = element_a.get('href')
                query_str = htmlparser.tools.queryString(element_a.get('href'))
                storage_data['id'] = query_str['resumeID']
                storage_data['data-userid'] = query_str['seekerUserID']
                storage_data['title'] = peo_item.get('title')
                storage_data['peo'].append(peo_item.get('title'))
            else:
                storage_data['peo'].append(peo_item.text)
        info_list = abstract.find_all("p")
        for info_item in info_list:
            storage_data['info'].append(info_item.text)
        result.append(storage_data)
    return result


def catchcv():
    htmlsource = source()
    bs = bs4.BeautifulSoup(htmlsource, 'lxml')
    recommand = bs.find(id='recommand-btn-area')
    recommand.decompose()
    send_contact = bs.find(id='haveSeenContact')
    send_contact.decompose()
    contact_type = bs.find(id='showContactType')
    contact_type.decompose()
    label = bs.find(class_='evalListsInnerBox')
    label_link = label.findAll('a')
    for e in label_link:
        e.decompose()
    detail_content = bs.find(class_='detail-con')
    resume_content = bs.find(class_='detail-tabs-new')
    return detail_content.prettify() + resume_content.prettify()
