from src.dao.user_dao import UserDao
from src.models.user import User
import bcrypt


class LoginController:

    def __init__(self, data):
        self.user = None
        self.data = data

    def get_user(self):
        return self.user

    def verify_credentials(self):
        dao = UserDao()
        self.user = dao.select_by_email(self.data['email'])
        if self.user:
            if check_pw(self.data['password'], self.user.password):
                return True
            return False
        return False

    def register(self):
        self.data['password'] = hash_pw(self.data['password'])
        self.user = User(self.data)
        dao = UserDao()
        status = dao.insert(self.user)
        if status:
            return "User registered successfully"
        return "Error registering user"


def hash_pw(pw):
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())


def check_pw(user_pw, bd_pw):
    return bcrypt.checkpw(user_pw.encode('utf-8'), bd_pw.encode('utf-8'))
