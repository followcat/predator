import urllib
import urllib2


class Urllib(objcet):

    def __init__(self):
        self._cookies = None

    @property
    def cookies(self):
        return self.cookies

    def set_cookies(self, cookies):
        """
            # cookies is a string
        """
        self._cookies = cookies

    def post(self, url, data=None, cookies=True):
        if data is None:
            data = {}
        headers = {}
        if cookies:
            headers['Cookie'] = self.cookies
        urllib_data = urllib.urlencode(data)
        req = urllib2.Request(url, headers = headers)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        res = opener.open(req, urllib_data)
        text = res.read()
        return text

    def get(self, url, cookies=True):
        headers = {}
        if cookies:
            headers['Cookie'] = self.cookies
        req = urllib2.Request(url, headers = headers)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        res = opener.open(req)
        text = res.read()
        return text

    
