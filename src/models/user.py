import datetime


class User:
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data.get('username', None)
        self.email = data.get('email', None)
        self.password = data.get('password', None)
        self.type = data.get('user_type', 0)
        self.created_at = data.get('created_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f"Id: {self.id} Name: {self.name} Email: {self.email} Password: {self.password} " \
               f"Type: {self.type} Created at: {self.created_at}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 4:
            raise ValueError('Name must be at least 4 characters long')
        self._name = name.title()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError('Email must be valid')
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        self._password = password
