import asyncio

import peewee_async
from tornado import web
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line

from project.application.handlers import UserListHandler, UserItemHandler, LoginHandler, LogoutHandler, \
    ProtectedHandler, TestModelListHandler
from project.application.models import db
from project.config.settings import debug, port, static_path, template_path

IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')


class MainHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')


settings = {
    'debug': debug,
    'template_path': template_path,
    'cookie_secret': '__GENERATE_RANDOM_VALUE__',
    'login_url': '/login',
}

application = web.Application([
    (r'/', MainHandler),
    (r'/user/([0-9]+)', UserItemHandler),
    (r'/user', UserListHandler),
    (r'/test_model', TestModelListHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/protected', ProtectedHandler),
    (r'/static/(.*)', web.StaticFileHandler, {'path': static_path}),
], **settings)

application.objects = peewee_async.Manager(db)


def run_tornado_server():
    parse_command_line()

    application.listen(port, '0.0.0.0')

    loop = asyncio.get_event_loop()
    loop.run_forever()
