from src.models.user import User


class Admin(User):
    def __init__(self, data):
        super().__init__(data)
