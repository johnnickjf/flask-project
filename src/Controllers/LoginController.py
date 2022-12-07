from http.client import HTTPSConnection
from base64 import b64encode


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


class LoginController:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == 'admin' and self.password == 'admin':
            return 'Welcome Admin'
        else:
            return 'Login failed'
