# -*- coding: utf-8 -*-
import time
import Queue
import functools
import threading

import utils.builtin
import storage.cv
import storage.jobtitles
import storage.fsinterface
import jobs.definition.cloudshare_jingying


class Batchconvert(jobs.definition.cloudshare_jingying.Jingying):

    CVDB_PATH = 'convert/jingying'
    #CVDB_PATH = 'additional/jingying'
    ORIGIN_CVDB_PATH = 'jingying_webdrivercv'

    def __init__(self):
        self.orinterface = storage.fsinterface.FSInterface(self.ORIGIN_CVDB_PATH)
        self.oristorage = storage.cv.CurriculumVitae(self.orinterface)

        self.fsinterface = storage.fsinterface.FSInterface(self.CVDB_PATH)
        self.cvstorage = storage.cv.CurriculumVitae(self.fsinterface)
        self.jtstorage = storage.jobtitles.JobTitles(self.fsinterface)
        self.save_yamldatas = []

    def jobgenerator(self, idlist):
        for classify_id in idlist:
            self.save_yamldatas = []
            yamlname = classify_id + '.yaml'
            yamldata = utils.builtin.load_yaml('jingying/JOBTITLES', yamlname)
            sorted_id = sorted(yamldata,
                               key = lambda cvid: yamldata[cvid]['peo'][-1],
                               reverse=True)
            for cv_id in sorted_id:
                if self.oristorage.exists(cv_id) and not self.cvstorage.exists(cv_id):
                    cv_info = yamldata[cv_id]
                    job_process = functools.partial(self.convertjob, cv_info)
                    yield job_process

    def convertjob(self, cv_info):
        cv_id = cv_info['id']
        print('Convert: '+cv_id)
        cv_content =  self.oristorage.get(cv_info['id'])
        yamldata = self.extract_details(cv_info, cv_content)
        return cv_content, cv_info['id'], yamldata


class ThreadConverter(threading.Thread):

    def __init__(self, name, queue, process_gen):
        super(ThreadConverter, self).__init__()
        self.name = name
        self.queue = queue
        self.process_gen = process_gen

    def run(self):
        while True:
            try:
                process_job = self.process_gen.next()
            except ValueError:
                time.sleep(0.1)
                continue
            except StopIteration as e:
                print(e)
                break
            cv_content, classify_id, summary = process_job()
            print(self.name, summary['id'])
            self.queue.put((cv_content, classify_id, summary))


class ThreadSaver(threading.Thread):

    def __init__(self, name, queue, cvstorage, jtstorage):
        super(ThreadSaver, self).__init__()
        self.name = name
        self.queue = queue
        self.cvstorage = cvstorage
        self.jtstorage = jtstorage
        self.yamldata = {}
        self.setDaemon(True)

    def run(self):
        while True:
            cv_content, classify_id, summary = self.queue.get()
            cv_id = summary['id']
            if classify_id not in self.yamldata:
                self.yamldata[classify_id] = []
            self.yamldata[classify_id].append(summary)
            self.cvstorage.add(cv_id, cv_content)
            #self.jtstorage.add_datas(classify_id, self.yamldata[classify_id])
            self.jtstorage.add_data(cv_id, summary)


if __name__ == '__main__':
    industry_yamls = ['47', #医疗设备/器械
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
                      '61'  #新能源
                    ]

    instance = Batchconvert()
    PROCESS_GEN = instance.jobgenerator(industry_yamls)
    queue_saver = Queue.Queue(0)
    t1 = ThreadConverter('1', queue_saver, PROCESS_GEN)
    t2 = ThreadConverter('2', queue_saver, PROCESS_GEN)
    t3 = ThreadConverter('3', queue_saver, PROCESS_GEN)
    t4 = ThreadConverter('4', queue_saver, PROCESS_GEN)


    saver = ThreadSaver('saver', queue_saver, instance.cvstorage, instance.jtstorage)

    saver.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
