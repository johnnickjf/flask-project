import datetime


class User:
    def __init__(self, data):
        self.__id = data.get('id', None)
        self.__name = data.get('username', None)
        self.__email = data['email']
        self.__password = data.get('password', None)
        self.__type = data.get('user_type', 0)
        self.__created_at = data.get('created_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f"Id: {self.__id} Name: {self.__name} Email: {self.__email} Password: {self.__password} " \
               f"Type: {self.__type} Created at: {self.__created_at}"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_type(self):
        return self.__type

    def get_created_at(self):
        return self.__created_at

    def set_id(self, user_id):
        self.__id = user_id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password
