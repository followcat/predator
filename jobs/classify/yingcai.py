#-*-utf-8-*-

import datetime
import math

import utils.builtin
import precedure.yingcai
import downloader._urllib
import downloader.webdriver
import storage.jobtitles
import storage.fsinterface

from sources.yingcai_all import *
from jobs.yingcai_needed import *
from sources.yingcai_liveplace import *

FF_PROFILE_PATH_LIST=['/home/winky/.mozilla/firefox/jvqqz5ch.winky',
                      '/home/winky/.mozilla/firefox/bs9yw52t.winky2',
                      '/home/winky/.mozilla/firefox/4idae7tm.winky3'
                     ]
profilepath_index=0
FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index]
START_TIME=datetime.datetime.now()

wbdriverdownloader = downloader.webdriver.Webdriver(profilepath=FF_PROFILE_PATH)
repo = storage.fsinterface.FSInterface('yingcai')
repojt = storage.jobtitles.JobTitles(repo)
yingcai=precedure.yingcai.Yingcai(wbdownloader=wbdriverdownloader)

for industry in job_list.keys():
    if len(job_list[industry].keys())==0:
        for key in industry_list[industry]:
            job_list[industry][key]=industry_list[indystry][key]
    for job in job_list[industry].keys():
        if len(job_list[industry][job])==0:
            job_list[industry][job]=industry_list[industry][job]
        for position in job_list[industry][job]:
            job_item=industry+','+job+','+position
            print job_item
            live_lists=[]
            chunk_len=5
            place_chunk=math.ceil(len(live_places)/chunk_len)
            for place_index in range(int(place_chunk)):
                live=''
                for index in range(chunk_len-1):
                    live+=(live_places[place_index*chunk_len+index]+';')
                live=live+(live_places[place_index*chunk_len+index+1])
                live_lists.append(live)

            block_size=10
            tot_block=15
            for live_index in range(0,len(live_lists)):
                live_place=live_lists[live_index]
                print live_place
                getdict = {
                        'jobType':1,
                        'live':live_place,
                        'jobs':job_item,
                        'page':'0'
                         }
                for index in range(0,tot_block):
                    minpage=index*block_size
                    maxpage=(index+1)*block_size
                    add_list=yingcai.update_classify(getdict,industry,repojt,minpage,maxpage)
                    if len(add_list)==0:
                        break
                    else:
                        id_str = industry
                        repojt.add_datas(id_str, add_list, 'winky')

                    current_time=datetime.datetime.now()
                    duration=(current_time-START_TIME).seconds
                    if duration > 1800:
                        wbdriverdownloader.close()
                        profilepath_index+=1
                        FF_PROFILE_PATH=FF_PROFILE_PATH_LIST[profilepath_index%len(FF_PROFILE_PATH_LIST)]
                        wbdriverdownloader = downloader.webdriver.Webdriver(profilepath=FF_PROFILE_PATH)
                        yingcai.wb_downloader=wbdriverdownloader
                        START_TIME=current_time
                    else:
                        continue
