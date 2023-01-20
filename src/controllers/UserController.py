from src.dao.ConnectionFactory import ConnectionFactory
from src.models.AdminModel import Admin
from src.models.UserModel import User


class UserController:

    def __init__(self):
        self.__User = None

    def get_user_by_id(self, user_id):
        connection = ConnectionFactory()
        result = connection.select(''' SELECT * FROM user WHERE id = %s ''',
                                   (user_id,))
        if result:
            self.__User = User({'id': result[0][0], 'username': result[0][1], 'email': result[0][2],
                                'user_type': result[0][4], 'created_at': result[0][5]})
            return self.__User
        return None
