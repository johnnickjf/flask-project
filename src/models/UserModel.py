class User:
    def __init__(self, name, email, password, tipo=0):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__type = tipo

    def __str__(self):
        return f"User {self.__name} is {self.__type} years old"

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_type(self):
        return self.__type

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password
