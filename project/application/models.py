from copy import deepcopy

import peewee
import peewee_async
from playhouse.db_url import parse

from project.application.utils import make_password
from project.config.settings import db_url

db_param = parse(db_url)

db = peewee_async.PooledPostgresqlDatabase(**db_param)


# Auth models


class User(peewee.Model):
    name = peewee.CharField(index=True, unique=True, verbose_name='Имя пользователя')
    password = peewee.CharField(verbose_name='Пароль')

    @classmethod
    async def create_user(cls, **kwargs):
        # Создание пользователя
        manager = peewee_async.Manager(db)
        param = deepcopy(kwargs)
        param['password'] = make_password(param['password'])
        return await manager.create(cls, **param)

    async def update_password(self, password):
        pass

    def __str__(self):
        return self.name

    class Meta:
        database = db


# Test models


class TestModel(peewee.Model):
    name = peewee.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        database = db
