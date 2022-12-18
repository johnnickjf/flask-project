from src.models.AdminModel import Admin
from src.models.UserModel import User

data = {'name': 'Joao', 'email': 'teste@gmail', 'password': '123456'}


user = User(data)
print(user.get_name())
print(user.get_email())
print(user.get_password())
print(user.get_type())
