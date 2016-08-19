import time
class NotImplementedInterface(Exception):
    pass

class Base(object):

    BASE_URL=''
    CLASSIFY_SLEEP = 5
    CLASSIFY_MAXPAGE = 20

    def __init__(self):
        self.url_downloader = url_downloader
        self.wb_downloader = wbdownloader

    def urlget_classify(self):
        raise NotImplementedInterface

    def urlget_cv(self):
        raise NotImplementedInterface

    def webdriverget_classify(self):
        raise NotImplementedInterface

    def webdriverget_cv(self):
        raise NotImplementedInterface

    def parse_classify(self):
        raise NotImplementedInterface

    def parse_cv(self):
        raise NotImplementedInterface

    def classify(self):
        raise NotImplementedInterface

    def cv(self,url):
        download_url=self.BASE_URL+url
        htmlsource=self.wb_downloader.getsource(download_url)
        result=self.parse_cv(htmlsource)
        return result

    def logException(self, text):
        with open('/tmp/classification.log', 'a+') as fp:
            fp.write(text)
        raise Exception(text)

    def update_classify(self, filename, id_str, postdict, repojt, header=None):
        add_list = []
        update_list = []
        for cur_page in range(self.CLASSIFY_MAXPAGE):
            postdict[self.PAGE_VAR] = cur_page + 1
            try:
                results = self.classify(postdict, header)
            except Exception:
                break
            if not results:
                break
            parts_results = []
            for result in results:
                if not repojt.exists(id_str, result['id']):
                    parts_results.append(result)
                else:
                    update_list.append(result)
            print 'current page:' + str(cur_page + 1)
            if len(parts_results) < len(results)*0.2:
                break
            else:
                add_list.extend(parts_results)
            time.sleep(self.CLASSIFY_SLEEP)
        head = {}
        head['postdict'] = header['postdict']
        repojt.add_datas(filename, add_list, update_list, head)
        return True
