from src.controllers.password_generator import PasswordGenerator


def test_password_generator():
    data = {'length': '8', 'number': True, 'especial': True}
    password = PasswordGenerator(data)
    assert password.password_generator() == 'a1b2c3d4'
