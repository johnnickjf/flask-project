from src.models.UserModel import User


class Admin(User):
    def __init__(self, data):
        super().__init__(data)
