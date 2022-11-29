from src.models.UserModel import User


class Admin(User):
    def __init__(self, name, email, password, age):
        super().__init__(name, email, password, age)
        self.__admin = True
