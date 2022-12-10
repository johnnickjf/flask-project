from flask import Flask
from src.routes import auth, homepage, password


app = Flask(__name__)

auth.configure(app)
homepage.configure(app)
password.configure(app)

if __name__ == '__main__':
    app.run(debug=True)
