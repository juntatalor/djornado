from peewee import IntegrityError
from tornado import web

from project.application import models_pb2
from project.application.base.handlers import ApiListHandler, ApiItemHandler, BaseHandler
from project.application.models import User, TestModel
from project.application.utils import check_password


# Auth handlers

class LoginHandler(BaseHandler):
    async def get(self):
        self.render('login.html', error='')

    async def post(self):
        name = self.get_argument('name')
        password = self.get_argument('password')
        no_redirect = self.get_argument('no_redirect', False)

        try:
            user = await self.application.objects.get(User, name=name)
        except User.DoesNotExist:
            self.render('login.html', error='User does not exist')
            return

        # ToDo: hash via executor (https://github.com/tornadoweb/tornado/blob/stable/demos/blog/blog.py#L208)
        if check_password(password, user.password.encode()):
            self.set_secure_cookie('user', str(user.id))
            if not no_redirect:
                # for testing purposes - only get Cookie in response, if no_redirect = True
                self.redirect(self.get_argument('next', '/'))
        else:
            self.render('login.html', error='Incorrect password')


class LogoutHandler(BaseHandler):
    async def get(self):
        self.clear_cookie('user')
        self.redirect(self.get_argument('next', '/'))


# User REST handler


class UserListHandler(ApiListHandler):
    model = User
    pb_item_cls = models_pb2.UserPB
    pb_list_cls = models_pb2.UserListPB

    async def create(self, save_dict):
        try:
            return await User.create_user(**save_dict)
        except IntegrityError:
            raise web.HTTPError(400)


class UserItemHandler(ApiItemHandler):
    model = User
    pb_item_cls = models_pb2.UserPB


# Protected hander for testing purposes


class ProtectedHandler(BaseHandler):
    @web.authenticated
    async def post(self):
        pass


# TestModel REST Handler


class TestModelListHandler(ApiListHandler):
    model = TestModel
    pb_item_cls = models_pb2.TestModelPB
    pb_list_cls = models_pb2.TestModelListPB
