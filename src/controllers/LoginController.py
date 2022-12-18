from src.dao.ConnectionFactory import ConnectionFactory
from src.models.UserModel import User
import bcrypt


class LoginController:

    def __init__(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def verify_credentials(self):
        connection = ConnectionFactory()
        result = connection.select(''' SELECT * FROM user WHERE email = %s ''',
                                   (self.__user['email'],))
        if result:
            if self.check_pw(self.__user['password'], result[0][3]):
                self.__user = User({'user_id': result[0][0], 'username': result[0][1],
                                    'email': result[0][2], 'password': result[0][3],
                                    'user_type': result[0][4], 'created_at': result[0][5]})
                return True
            return False
        return False

    def register(self):
        user = User(self.__user)
        query = ''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s, %s) '''
        values = (user.get_name(), user.get_email(), self.encode_pw(user.get_password()),
                  user.get_type(), user.get_created_at())
        connection = ConnectionFactory()
        status = connection.insert(query, values)
        if status:
            return "User registered successfully"
        return "Error registering user"

    # alter for bcrypt
    @staticmethod
    def encode_pw(pw):
        return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def check_pw(user_pw, bd_pw):
        return bcrypt.checkpw(user_pw.encode('utf-8'), bd_pw.encode('utf-8'))
