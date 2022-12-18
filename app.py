from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from src.routes import auth, homepage, password
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta
import os

load_dotenv(find_dotenv('.env'))

app = Flask(__name__)
JWTManager(app)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
auth.configure(app)
homepage.configure(app)
password.configure(app)


# temporary file for testing
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
