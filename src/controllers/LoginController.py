from base64 import b64encode, b64decode
from src.dao.ConnectionFactory import ConnectionFactory
from src.models.UserModel import User
import datetime


class LoginController:

    def __init__(self, email, password, nickname=None):
        self.__nickname = nickname
        self.__email = email
        self.__password = password
        self.__user = None

    def verify_credentials(self):
        connection = ConnectionFactory()
        result = connection.select(''' SELECT * FROM user WHERE email = %s AND password = %s ''',
                                   (self.__email, self.encode(self.__password)))
        if result:
            self.__user = User(result[0][1], result[0][2], result[0][3], result[0][4], result[0][0])
            return True
        return False

    def register(self):
        self.__user = User(self.__nickname, self.__email, self.__password)
        query = ''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s) '''
        values = (self.__user.get_name(), self.__user.get_email(), self.encode(self.__user.get_password()),
                  self.__user.get_type())
        connection = ConnectionFactory()
        status = connection.insert(query, values)
        if status:
            return "User registered successfully"
        return "Error registering user"

    # alter for jwt
    def create_token(self):
        return b64encode(bytes(str(self.__user.get_id()) + ';' +
                               str(self.__user.get_name() + ';' +
                               str(self.__user.get_type()) + ';' +
                               datetime.datetime.now().strftime('%X')), 'utf-8')).decode('utf-8')

    # alter for bcrypt
    @staticmethod
    def encode(x):
        return b64encode(bytes(x, 'utf-8')).decode('utf-8')

    @staticmethod
    def decode(x):
        return b64decode(x).decode('utf-8')
