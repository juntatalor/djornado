import peewee
import pytest

from project.application.models import User


def test_models_sync():
    # Проверка невозможности работы с бд в синхронном режиме
    with pytest.raises(AssertionError):
        User.create(name='FailName', password='FailPwd')


@pytest.mark.gen_test
async def test_user_async(app):
    # Проверка создания пользователя
    user = await app.objects.create(User, name='TestName', password='TestPwd')
    assert user.name, user.password == ('TestName', 'TestPwd')
    assert str(user) == 'TestName'

    with pytest.raises(peewee.IntegrityError):
        # Проверка уникальности
        await app.objects.create(User, name='TestName', password='TestPwd')

    # Проверка update
    user.name = 'NewTestName'
    await app.objects.update(user)
    assert user.name == 'NewTestName'

    # Проверка delete & count
    await app.objects.delete(user)
    user_cnt = await app.objects.count(User.select())
    assert user_cnt == 0

    # Необходимо не забывать закрывать соединение
    await app.objects.close()
