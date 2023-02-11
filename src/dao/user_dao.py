from src.dao.connection_factory import ConnectionFactory
from src.models.user import User


class UserDao(ConnectionFactory):

    def __init__(self):
        super().__init__()

    def insert(self, user):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s, %s) ''',
                           (user.name, user.email, user.password,
                            user.type, user.created_at))
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def select(self, user_id):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' SELECT * FROM user WHERE id = %s ''', (user_id,))
            result = cursor.fetchall()
            cursor.close()
            return create_user(result)
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def select_by_email(self, email):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' SELECT * FROM user WHERE email = %s ''', (email,))
            result = cursor.fetchall()
            cursor.close()
            return create_user(result)
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def update(self, user):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' UPDATE user SET name = %s, email = %s, password = %s WHERE id = %s ''',
                           (user.name, user.email, user.password, user.id))
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def delete(self, user_id):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' DELETE FROM user WHERE id = %s ''', (user_id,))
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def delete_by_email(self, email):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(''' DELETE FROM user WHERE email = %s ''', (email,))
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False


def create_user(result):
    return User({'id': result[0][0], 'username': result[0][1],
                 'email': result[0][2], 'password': result[0][3],
                 'user_type': result[0][4], 'created_at': result[0][5]})
