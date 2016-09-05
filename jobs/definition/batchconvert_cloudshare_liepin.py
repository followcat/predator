import Queue

import jobs.definition.cloudshare_liepin
from jobs.definition.batchconvert import *


class Batchconvert(BatchconvertCloudshare,
                   jobs.definition.cloudshare_liepin.Liepin):

    CVDB_PATH = 'convert/liepin'
    ORIGIN_CVDB_PATH = 'output/liepin'

    def extract_details(self, uploaded_details, cv_content):
        details = super(Batchconvert, self).extract_details(uploaded_details, cv_content)
        details['date'] = uploaded_details['date']
        return details


if __name__ == '__main__':
    instance = Batchconvert()
    PROCESS_GEN = instance.jobgenerator('output/liepin/JOBTITLES')

    queue_saver = Queue.Queue(0)
    t1 = ThreadConverter('1', queue_saver, PROCESS_GEN)
    t2 = ThreadConverter('2', queue_saver, PROCESS_GEN)
    t3 = ThreadConverter('3', queue_saver, PROCESS_GEN)
    t4 = ThreadConverter('4', queue_saver, PROCESS_GEN)

    saver = ThreadSaver('saver', queue_saver, instance.cvstorage)

    saver.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
