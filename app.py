from flask import Flask
from dotenv import load_dotenv, find_dotenv
from routes import login, register, homepage, password

load_dotenv(find_dotenv('.env'))

app = Flask(__name__)

register.configure(app)
login.configure(app)
homepage.configure(app)
password.configure(app)

if __name__ == '__main__':
    app.run(debug=True)
