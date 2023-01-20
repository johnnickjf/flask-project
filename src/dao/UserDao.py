from src.dao.ConnectionFactory import ConnectionFactory


class UserDao(ConnectionFactory):

    def __init__(self):
        super().__init__()
