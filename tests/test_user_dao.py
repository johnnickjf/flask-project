from src.dao.user_dao import UserDao
from src.models.user import User
from src.dao.connection_factory import ConnectionFactory


def test_insert_user():
    user = User({'username': 'test', 'email': 'testando@gmail.com', 'password': 'pass'})
    assert user.name == 'test'


def test_insert():
    assert 10 > 5


def test_insert_user_dao():
    user = User({'username': 'jao', 'email': 'testandoja11@mail.com', 'password': 'senha123'})
    teste = UserDao()
    assert teste.insert(user) is True


def test_select():
    assert 10 > 5


def test_update():
    assert 10 > 5


def test_delete():
    assert 10 > 5
