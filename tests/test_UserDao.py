from src.models.UserModel import User
from src.dao.ConnectionFactory import ConnectionFactory


def test_insert_user():
    user = User('test', 'testando@gmail.com', 'pass')
    print(user)
    assert user.get_name() == 'test'


def test_insert():
    user = User('test', 'alpha', 'pass')
    connection = ConnectionFactory()
    query = "INSERT INTO user (`name`, email, password) VALUES (%s, %s, %s)"
    values = (user.get_name(), user.get_email(), user.get_password())
    connection.insert(query, values)
    assert user.get_name() == 'test'
