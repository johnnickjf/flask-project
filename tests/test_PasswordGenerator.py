from src.controllers.PasswordGenerator import PasswordGenerator


def test_password_generator():
    data = {'length': '8', 'number': '1', 'especial': '1'}
    password = PasswordGenerator(data)
    assert password.password_generator() == {'password': 'xZyYlLwW'}
