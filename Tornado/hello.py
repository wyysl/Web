# encoding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello Itcast')


if __name__ == '__main__':

    app = tornado.web.Application([
        (r'/', IndexHandler),

    ])

    # app.listen(8000)

    http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8080)

    http_server.bind(8009)
    http_server.start(0)

    tornado.ioloop.IOLoop.current().start()
