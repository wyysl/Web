
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define, options
from tornado.web import RequestHandler, url

tornado.options.define('port', type=int, default=8101, help='hahaha')


class IndexHandler(RequestHandler):

    def get(self):

       # f = self.request.files["image1"]
       	print type(self.request.files)
        print self.request.files.keys()
        self.request.files['image'][0]['body']

        file = open('./itcast','w')
        file.write('image_file')
        file.close()

        self.write("OK")





if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application([

        (r'/', IndexHandler),

    ],
        debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
