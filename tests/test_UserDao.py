from src.models.UserModel import User
from src.dao.UserDao import UserDao


def test_insert_user():
    user = User('test', 'testando@gmail.com', 'pass')
    print(user)
    assert user.get_name() == 'test'

def test_insert_user():
    user = User('test', 'abelha', 'pass')
    dao = UserDao()
    dao.insert_user(user)
    assert user.get_name() == 'test'