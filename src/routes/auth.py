from flask import Blueprint, render_template, request, jsonify
from src.controllers.LoginController import LoginController

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        valid = LoginController(request.form.get('email'), request.form.get('password'))
        if valid.verify_credentials():
            return jsonify({'token': valid.create_token()})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    new_user = LoginController(request.form.get('email'), request.form.get('password'), request.form.get('nickname'))
    return jsonify({'status': new_user.register()})


def configure(app):
    app.register_blueprint(bp)
