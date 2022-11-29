class LoginController:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def login(self):
        if self.user == 'admin' and self.password == 'admin':
            return 'Welcome Admin'
        else:
            return 'Login failed'
