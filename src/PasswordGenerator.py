import random

CHAR = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
NUM = '0123456789'
ESP = '[]{}()*#;/,-_%'


def password_generator(data):
    password = {'password': ''}
    aux = CHAR
    if int(data['especial']):
        aux += ESP
    if int(data['number']):
        aux += NUM
    password['password'] = ''.join(random.sample(aux, int(data['length'])))
    return password
