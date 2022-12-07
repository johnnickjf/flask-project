import random


class PasswordGenerator:
    def __init__(self, data):
        self.__str = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        self.__num = '0123456789'
        self.__esp = '[]{}()*#;/,-_%'
        self.__data = data

    def create_str(self):
        if self.__data.get('number'):
            self.__num += self.__num
        if self.__data.get('especial'):
            self.__esp += self.__esp

    def password_generator(self):
        self.create_str()
        password = {'password': ''.join(random.sample(self.__str, int(self.__data['length'])))}
        return password
