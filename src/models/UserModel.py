class User:
    def __init__(self, name, email, password, age):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__age = age

    def __str__(self):
        return f"User {self.__name} is {self.__age} years old"

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_age(self, age):
        self.__age = age
