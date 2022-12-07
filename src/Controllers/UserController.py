from src.models.AdminModel import Admin
from src.models.UserModel import User
from src.dao.UserDao import UserDao

user = User('test', 'caca', 'asda')
print(user.get_name())
print(user.get_email())
print(user.get_password())
print(user.get_type())

admin = Admin('admin', 'asda', 'asdasd')
print(admin.get_name())
print(admin.get_email())
print(admin.get_password())
print(admin.get_type())


dao = UserDao()
dao.insert_user(user)
