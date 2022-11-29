from src.models.CalculadoraModel import Calculadora
from src.models.UserModel import User

calcu = Calculadora()

user = User('jooq', 'email@gmail.com', 'senna123', 10)

user.set_age(20)

print(user)
