from src.dao.ConnectionFactory import ConnectionFactory
from src.dao.UserDao import UserDao
from src.models.AdminModel import Admin
from src.models.UserModel import User


class UserController:

    def __init__(self):
        self.__user = None

    def get_user_by_id(self, user_id):
        dao = UserDao()
        self.__user = dao.select(user_id)
        if self.__user:
            return self.__user
        return 'User not found'

