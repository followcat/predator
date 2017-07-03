# -*- coding: utf-8 -*-
import bs4
import time

import flask
import flask_restful
from flask_restful import Resource, reqparse

import tools.image


class LiepinPluginSyncObject(object):

    committer = 'PLUGIN'

    def __init__(self, url, htmlsource, base64email, base64phone):
        self.url = url
        self.htmlsource = htmlsource
        self.base64email = base64email
        self.base64phone = base64phone
        self.raw_html, self.raw_yaml = self.parse_source()
        self.info = self.generate_yaml()
        self.loginfo = ''
        self.parse_result = False

    def generate_yaml(self):
        info = dict()
        info.update(self.raw_yaml)
        info['committer'] = 'PLUGIN'
        info['origin'] = u'猎聘爬取'
        #info['email'] = self.email_from_base64()
        #info['phone'] = self.phone_from_base64()
        return info

    def email_from_base64(self):
        img = tools.image.image_from_base64(self.base64email)
        preimg = tools.image.preprocess(img)
        result = tools.image.image_to_string(preimg)
        return result.replace(' ', '')

    def phone_from_base64(self):
        img = tools.image.image_from_base64(self.base64phone)
        preimg = tools.image.preprocess(img)
        result = tools.image.image_to_string(preimg)
        return result.replace(' ', '')

    def parse_source(self):
        bs = bs4.BeautifulSoup(self.htmlsource, 'lxml')

        details = dict()
        details['date'] = time.time()
        details['filename'] = self.url
        idtag = bs.find('span', attrs={'data-nick':'res_id'})
        details['id'] = idtag.text
        details['originid'] = idtag.text

        login_form = bs.find(class_='user-login-reg')
        if login_form is not None:
            self.loginfo = 'NoLoginError'
            self.parse_result = False
            return '', {}
        side = bs.find(class_='side')
        side.decompose()
        footer = bs.find('footer')
        footer.decompose()
        javascripts = bs.findAll('script')
        for js in javascripts:
            js.decompose()
        alinks = bs.findAll('a')
        for a in alinks:
            a.decompose()
        content = bs.find(class_='resume')
        self.parse_result = True
        return content.prettify(), details

    def add_new(self, cvstorage):
        result = False
        if self.info['id']:
            if len(self.raw_html) < 500:
                self.loginfo = (' ').join([self.info['id'], 'too short.'])
            else:
                if not cvstorage.exists(self.info['id']):
                    result = cvstorage.addcv(self.info['id'],
                                             self.raw_html.encode('utf-8'), self.info)
                else:
                    self.loginfo = (' ').join([self.info['id'], 'exists'])
        else:
            self.loginfo = "without ID."
        if result is True:
            print((' ').join(["Plugin add Liepin", self.info['id']]))
        else:
            print((' ').join(["Plugin add Liepin failed", self.loginfo]))
        return result


class BrowserSyncAPI(Resource):

    def __init__(self):
        super(BrowserSyncAPI, self).__init__()
        self.reqparse = reqparse.RequestParser()
        self.LIEPIN_STO_CV = flask.current_app.config['LIEPIN_STO_CV']
        self.reqparse.add_argument('url', type = unicode, location = 'json')
        self.reqparse.add_argument('html', type = unicode, location = 'json')
        self.reqparse.add_argument('base64email', type = unicode, location = 'json')
        self.reqparse.add_argument('base64phone', type = unicode, location = 'json')

    def post(self):
        args = self.reqparse.parse_args()
        url = args['url']
        html = args['html']
        base64email = args['base64email']
        base64phone = args['base64phone']
        id = ''
        result = False
        if 'liepin' in url:
            lpso = LiepinPluginSyncObject(url, html, base64email, base64phone)
            result = lpso.add_new(self.LIEPIN_STO_CV)
        if result is True:
            id = lpso.info['id']
        return {'code': 200, 'url': url, 'result': result, 'id': id}


app = flask.Flask(__name__)
app.config.from_object('plugins.server.settings')
api = flask_restful.Api(app)
api.add_resource(BrowserSyncAPI, '/api/browsersync', endpoint = 'browsersync')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5888, threaded=True)
