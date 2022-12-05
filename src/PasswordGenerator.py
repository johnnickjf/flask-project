import random

CHAR = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
NUM = '0123456789'
ESP = '[]{}()*#;/,-_%'


def password_generator(length, number, especial):
    password = ''
    aux = CHAR
    if especial:
        aux += ESP
    if number:
        aux += NUM
    password = ''.join(random.sample(aux, length))
    return password
