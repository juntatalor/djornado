from http.cookies import SimpleCookie
from urllib.parse import urlencode

import pytest
from tornado.httpclient import HTTPError

from project.application import models_pb2
from project.application.models import TestModel, User
from project.application.utils import make_password


@pytest.mark.gen_test
async def test_root(http_client, base_url):
    response = await http_client.fetch(base_url)
    assert response.code == 200


static_files = ['css/bootstrap.min.css',
                'js/bootstrap.min.js',
                'js/jquery-3.1.0.min.js']


@pytest.mark.gen_test
@pytest.mark.parametrize('static_file', static_files)
async def test_static_bootstrap(http_client, base_url, static_file):
    response = await http_client.fetch(base_url + '/static/%s' % static_file)
    assert response.code == 200


@pytest.fixture
def login_test_user(request, async_db):
    """
    Creates test user for login test
    """
    with async_db.allow_sync():
        user = User.create(name='LoginTestUser', password=make_password('TestPassword'))

    def teardown():
        with async_db.allow_sync():
            User.delete_instance(user)

    request.addfinalizer(teardown)


@pytest.fixture
def user_cleanup(request, async_db):
    """
    Cleanup for user table
    """

    def teardown():
        with async_db.allow_sync():
            User.delete().execute()

    request.addfinalizer(teardown)


@pytest.mark.gen_test
async def test_user_handler(http_client, base_url, monkeypatch, user_cleanup):
    # Set authentication
    monkeypatch.setattr('project.application.base.handlers.BaseHandler.get_current_user', lambda x: 'TestUser')

    # Create user
    user = models_pb2.UserPB()
    user.name = 'TestUser'
    user.password = 'TestPassword'
    resp = await http_client.fetch(base_url + '/user', method='POST', body=user.SerializeToString())
    assert resp.code == 201

    # Create user - Integrity error
    user = models_pb2.UserPB()
    user.name = 'TestUser'
    user.password = 'TestPassword'
    with pytest.raises(HTTPError) as e:
        await http_client.fetch(base_url + '/user', method='POST', body=user.SerializeToString())
    assert e.value.code == 400

    # Get user list
    resp = await http_client.fetch(base_url + '/user')
    assert resp.code == 200
    user_list = models_pb2.UserListPB.FromString(resp.body)
    assert hasattr(user_list, 'items')
    assert len(user_list.items) == 1
    assert user_list.items[0].name == 'TestUser'

    # Delete user
    resp = await http_client.fetch(base_url + '/user/%s' % user_list.items[0].id, method='DELETE')
    assert resp.code == 204


@pytest.mark.gen_test
async def test_login_handler(http_client, base_url, app, login_test_user):

    resp = await http_client.fetch(base_url + '/login')
    assert resp.code == 200

    # Incorrect username
    body = {'name': 'IncorrectUser', 'password': 'TestPassword'}
    resp = await http_client.fetch(base_url + '/login', method='POST', body=urlencode(body))
    assert 'User does not exist' in resp.body.decode()

    # Incorrect password
    body = {'name': 'LoginTestUser', 'password': 'IncorrectPassword'}
    resp = await http_client.fetch(base_url + '/login', method='POST', body=urlencode(body))
    assert 'Incorrect password' in resp.body.decode()

    # Login
    body = {'name': 'LoginTestUser', 'password': 'TestPassword', 'no_redirect': True}
    response = await http_client.fetch(base_url + '/login', method='POST', body=urlencode(body))
    assert response.code == 200
    auth_cookie = SimpleCookie()
    auth_cookie.load(response.headers['Set-Cookie'])

    # Fetch login-required url without authentication
    with pytest.raises(HTTPError) as e:
        await http_client.fetch(base_url + '/protected', method='POST', body='')
    assert e.value.code == 403

    # Fetch login-required url with authentication
    response = await http_client.fetch(base_url + '/protected', method='POST', body='',
                                       headers={'Cookie': 'user=%s' % auth_cookie['user']})
    assert response.code == 200

    await app.objects.close()


@pytest.mark.gen_test
async def test_logout_handler(http_client, base_url, monkeypatch):
    # Set authentication
    monkeypatch.setattr('project.application.base.handlers.BaseHandler.get_current_user', lambda x: 'TestUser')

    # Fetch login-required url with authentication
    resp = await http_client.fetch(base_url + '/board')
    assert resp.code == 200

    resp = await http_client.fetch(base_url + '/logout')
    assert resp.code == 200

    monkeypatch.undo()

    # Fetch login-required url without authentication
    with pytest.raises(HTTPError) as e:
        await http_client.fetch(base_url + '/board', method='POST', body='')
    assert e.value.code == 403


@pytest.mark.gen_test
async def test_test_model_api(http_client, base_url, monkeypatch):
    # Set authentication
    monkeypatch.setattr('project.application.base.handlers.BaseHandler.get_current_user', lambda x: 'TestUser')

    # Create board via API
    test_model = models_pb2.TestModelPB()
    test_model.id_item = 1
    test_model.name = 'TestModel'
    resp = await http_client.fetch(base_url + '/test_model', method='POST', body=test_model.SerializeToString())
    assert resp.code == 201

    # Get boards
    res = await http_client.fetch(base_url + '/test_model')
    assert res.code == 200

    test_models = models_pb2.TestModelListPB.FromString(res.body)

    assert hasattr(test_models, 'items')
    assert len(test_models.items) == 1
    assert test_models.items[0].id_item == 1
    assert test_models.items[0].name == 'TestModel'
