from src.models.AdminModel import Admin
from src.models.UserModel import User
import bcrypt

user = User('user', 'teste', 'teste')
print(user.get_name())
print(user.get_email())
print(user.get_password())
print(user.get_type())

admin = Admin('admin', 'teste', 'teste')
print(admin.get_name())
print(admin.get_email())
print(admin.get_password())
print(admin.get_type())

password = str(input("input password: "))

password = password.encode('utf-8')

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

check = str(input("check password: "))

check = check.encode('utf-8')

if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")
