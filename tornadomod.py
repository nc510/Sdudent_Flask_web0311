# 一世无尘
# 倾尽温柔
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
import app

http_server = HTTPServer(WSGIContainer(app.app_0))

http_server.bind(5000, "0.0.0.0")

http_server.start(1)

http_server.listen(9696)

IOLoop.instance().start()
