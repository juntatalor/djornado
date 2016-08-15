import logging
import os

from manager import Manager
from peewee_migrate import Router

from project.app import run_tornado_server
from project.application.models import db
from project.config.settings import base_dir

manager = Manager()

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@manager.command
def runserver():
    """Runs tornado server"""
    run_tornado_server()


@manager.command
def makemigrations(name='auto'):
    """
    Makes migrations
    """
    migrator = Router(db, logger=LOGGER)
    migrator.migrate_dir = os.path.join(base_dir, 'application', 'migrations')
    migrator.create(name=name, auto='project.application.models')


@manager.command
def migrate(name=None):
    """
    Runs migrations
    """
    migrator = Router(db, logger=LOGGER)
    migrator.migrate_dir = os.path.join(base_dir, 'application', 'migrations')
    migrator.run(name=name)


@manager.command
def rollback(name):
    """
    Rolls back migration
    """
    migrator = Router(db, logger=LOGGER)
    migrator.migrate_dir = os.path.join(base_dir, 'application', 'migrations')
    migrator.rollback(name)


if __name__ == '__main__':
    manager.main()
