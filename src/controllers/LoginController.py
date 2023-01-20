from src.dao.UserDao import UserDao
from src.models.UserModel import User
import bcrypt


class LoginController:

    def __init__(self, data):
        self.__user = None
        self.__data = data

    def get_user(self):
        return self.__user

    def verify_credentials(self):
        dao = UserDao()
        self.__user = dao.select_by_email(self.__data['email'])
        if self.__user:
            if self.check_pw(self.__data['password'], self.__user.get_password()):
                return True
            return False
        return False

    def register(self):
        self.__data['password'] = self.hash_pw(self.__data['password'])
        self.__user = User(self.__data)
        dao = UserDao()
        status = dao.insert(self.__user)
        if status:
            return "User registered successfully"
        return "Error registering user"

    @staticmethod
    def hash_pw(pw):
        return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def check_pw(user_pw, bd_pw):
        return bcrypt.checkpw(user_pw.encode('utf-8'), bd_pw.encode('utf-8'))
