from src.Controllers.PasswordGenerator import password_generator


def test_password_generator():
    data = {'length': '8', 'number': '1', 'especial': '1'}
    password = password_generator(data)
    assert len(password['password']) == 8
    assert password['password'].isalnum() is False
