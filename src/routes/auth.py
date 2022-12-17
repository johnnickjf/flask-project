from flask import Blueprint, request, jsonify, render_template
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from src.controllers.LoginController import LoginController
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))

bp = Blueprint('auth', __name__, url_prefix='/auth')


# temporary file for testing
@bp.route('/login')
def login_html():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login():
    data = LoginController(request.json)
    if data.verify_credentials():
        return jsonify({'access_token': create_access_token(data.get_user().get_id(), expires_delta=timedelta(hours=1)),
                        'refresh_token': create_refresh_token(data.get_user().get_id(),
                                                              expires_delta=timedelta(days=7)),
                        'status': 'success'}), 200
    return jsonify({'status': 'Invalid credentials'}), 401


# temporary file for testing
@bp.route('/register', methods=['GET'])
def register_html():
    return render_template('register.html')


@bp.route('/env', methods=['GET'])
def get_env():
    return os.getenv('USER') + "<br>" + os.getenv('PASSWORD') + "<br>" + os.getenv('HOST') + "<br>" + os.getenv('DATABASE')


@bp.route('/register', methods=['POST'])
def register():
    if request.json['username'] == '' or request.json['email'] == '' or request.json['password'] == '':
        return jsonify({'status': 'fill in all fields'}), 401
    user = LoginController(request.json)
    return jsonify({'status': user.register()})


def configure(app):
    app.register_blueprint(bp)
