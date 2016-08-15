"""
General fixtures for Tornado application testing
"""

import os
from subprocess import Popen

import pytest
from peewee_migrate import Router
from playhouse.db_url import parse

from project.app import application
from project.application.models import db
from project.config.settings import base_dir, db_url

db_param = parse(db_url)
TEST_DB = db_param['database']


@pytest.fixture(scope='session')
def app():
    return application


@pytest.fixture(scope='session', autouse=True)
def async_db(request):
    """
    Фикстура для асинхронного взаимодействия с базой PostgreSQL через PeeWee ORM
    """
    # Создание базы
    process = Popen(['createdb', TEST_DB])
    process.communicate()
    db.allow_sync = True
    # Миграции
    migrator = Router(db)
    migrator.migrate_dir = os.path.join(base_dir, 'application', 'migrations')
    migrator.run()

    db.allow_sync = False

    def teardown():
        terminate_sql = ("SELECT pg_terminate_backend(pg_stat_activity.pid) "
                         "FROM pg_stat_activity "
                         "WHERE pg_stat_activity.datname = '%s' "
                         "AND pid <> pg_backend_pid();" % TEST_DB)
        process = Popen(['psql', '-c', terminate_sql])
        process.communicate()
        process = Popen(['dropdb', TEST_DB])
        process.communicate()

    request.addfinalizer(teardown)
    return db
