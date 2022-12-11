from flask import Blueprint, render_template, request, jsonify
from src.controllers.LoginController import LoginController

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    valid = LoginController(request.form)
    if valid.verify_credentials():
        return jsonify({'token': valid.create_token()}), 200
    return jsonify({'error': 'Invalid credentials'}), 401


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.form.get('username') == '' or request.form.get('email') == '' or request.form.get('password') == '':
        return jsonify({'status': 'fill in all fields'}), 401
    user = LoginController(request.form)
    return jsonify({'status': user.register()})


def configure(app):
    app.register_blueprint(bp)
