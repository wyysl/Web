import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json

from tornado.web import RequestHandler
from tornado.options import define, options

define('port', default=8087, type=int)


class IndexHandler(RequestHandler):

	def set_default_headers(self):
		self.set_header('Content-Type', 'application/json')
		self.set_header('itcast', 'python')

    def get(self):
        # self.write("hello itcast1<br/>")
        # self.write("hello itcast2<br/>")
        # self.write("hello itcast3<br/>")

        stu = {

            'name': 'zhangsan',
            'age': '23',
            'gender': '1',

        }

        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header('itcast','CPP')
        self.set_status(211)



    def post(self):
    	stu = {

            'name': 'zhangsan',
            'age': '24',
            'gender': '1',

        }

        stu_json = json.dumps(stu)
        self.write(stu_json)


        self.set_header('itcast','cpp')
        self.set_status(404)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([

        (r'/', IndexHandler),

    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
