from src.dao.ConnectionFactory import ConnectionFactory

class UsarDao(ConnectionFactory):

        def __init__(self, app):
            super().__init__(app)

        def register(self, user):
            cursor = self.connect()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (user.name, user.email, user.password))
            cursor.connection.commit()
            cursor.close()

        def login(self, user):
            cursor = self.connect()
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (user