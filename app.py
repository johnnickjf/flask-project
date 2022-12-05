from flask import Flask, request, render_template
from src.LoginController import LoginController
from src.PasswordGenerator import password_generator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/api/password', methods=['GET'])
def password_gen():
    length = request.args.get('length')
    number = request.args.get('number')
    especial = request.args.get('especial')
    return password_generator(int(length), int(number), int(especial))


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def authentication():
    nickname = request.form.get('nickname')
    password = request.form.get('password')
    login_controller = LoginController(nickname, password)
    return login_controller.login()


@app.route('/success/<user>', methods=['GET'])
def success_auth(user):
    return f'Parabens {user}'


if __name__ == '__main__':
    app.run(debug=True)
