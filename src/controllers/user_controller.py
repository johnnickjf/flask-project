from src.dao.user_dao import UserDao
from src.models.user import User
from src.controllers.login_controller import hash_pw


class UserController:

    def __init__(self):
        self.__user = None

    def get_user_by_id(self, user_id):
        dao = UserDao()
        self.__user = dao.select(user_id)
        if self.__user:
            return self.__user
        return 'User not found'

    def update_user_by_id(self, data):
        dao = UserDao()
        data['password'] = hash_pw(data['password'])
        self.__user = User(data)
        status = dao.update(self.__user)
        if status:
            return 'User updated successfully'
        return 'Error updating user'
