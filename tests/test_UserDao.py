from src.models.UserModel import User
from src.dao.ConnectionFactory import ConnectionFactory


def test_insert_user():
    user = User('test', 'testando@gmail.com', 'pass')
    assert user.get_name() == 'test'


def test_insert():
    user = User('Joao', 'email@gmail.com', 'secret123')
    connection = ConnectionFactory()
    assert connection.insert(''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s) ''',
                             (user.get_name(), user.get_email(), user.get_password(), user.get_type())) is True


def test_select():
    connection = ConnectionFactory()
    user = connection.select(''' SELECT * FROM user WHERE email = %s ''', ('email@gmail.com',))
    print(user[0])
    assert connection.select(''' SELECT * FROM user WHERE email = %s ''', ('email@gmail.com',)) is not False
    

def test_update():
    connection = ConnectionFactory()
    assert connection.update(''' UPDATE user SET nome = %s WHERE email = %s ''',
                             ('Joao', 'email@gmail.com')) is True


def test_delete():
    connection = ConnectionFactory()
    assert connection.delete(''' DELETE FROM user WHERE email = %s ''', ('email@gmail.com',)) is True
