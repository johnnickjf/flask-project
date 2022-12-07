from flask import Flask, request, render_template
from src.Controllers.PasswordGenerator import password_generator
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv, find_dotenv
# from routes import login, register, homepage


load_dotenv(find_dotenv('.env'))

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DATABASE')

mysql = MySQL(app)


# register.configure(app)
# login.configure(app)
# homepage.configure(app)


def insert(query, values):
    cursor = mysql.connection.cursor()
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()


def select(query, values):
    cursor = mysql.connection.cursor()
    cursor.execute(query, values)
    data = cursor.fetchall()
    cursor.close()
    return data


@app.route('/api/password', methods=['GET'])
def password_gen():
    return password_generator(request.args)


@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = select('''SELECT * FROM user WHERE email = %s AND password = %s''',
                      (request.form.get('email'), request.form.get('password')))
        print(len(data) > 0)
        if len(data) > 0:
            return render_template('homepage.html')
        else:
            return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        nome_user = request.form.get('nickname')
        email_user = request.form.get('email')
        pass_user = request.form.get('password')
        insert(''' INSERT INTO user VALUES(NULL, %s, %s, %s, %s) ''', (nome_user, email_user, pass_user, 0))
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
