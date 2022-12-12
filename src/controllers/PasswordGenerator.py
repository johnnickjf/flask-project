import random


class PasswordGenerator:
    def __init__(self, data):
        self.__str = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        self.__num = '0123456789'
        self.__esp = '[]{}()*#;/,-_%'
        self.__data = data

    def create_str(self):
        if self.__data['number']:
            self.__str += self.__num
        if self.__data['esp']:
            self.__str += self.__esp

    def password_generator(self):
        self.create_str()
        password = {'password': ''.join(random.sample(self.__str, int(self.__data['length'])))}
        return password
