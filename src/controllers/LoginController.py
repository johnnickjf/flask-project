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
                self.__user = User(result[0][1], result[0][2], result[0][3], result[0][4], result[0][0])
                return self.__user
            return False
        return False

    def register(self):
        self.__user = User(self.__user['username'], self.__user['email'], self.__user['password'])
        query = ''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s) '''
        values = (self.__user.get_name(), self.__user.get_email(), self.encode_pw(self.__user.get_password()),
                  self.__user.get_type())
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
