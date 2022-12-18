from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from src.controllers.LoginController import LoginController

bp = Blueprint('auth', __name__, url_prefix='/auth')


# temporary file for testing
@bp.route('/login')
def login_html():
    return render_template('login.html')


# temporary file for testing
@bp.route('/register', methods=['GET'])
def register_html():
    return render_template('register.html')


@bp.route('/login', methods=['POST'])
def login():
    data = LoginController(request.json)
    if data.verify_credentials():
        return jsonify({'access_token': create_access_token(identity=data.get_user().get_id()),
                        'refresh_token': create_refresh_token(identity=data.get_user().get_id()),
                        'message': 'Valid credentials'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401


@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    return jsonify({'access_token': create_access_token(identity=identity)}), 200


@bp.route('/register', methods=['POST'])
def register():
    if request.json['username'] == '' or request.json['email'] == '' or request.json['password'] == '':
        return jsonify({'message': 'fill in all fields'}), 401
    user = LoginController(request.json)
    return jsonify({'message': user.register()})


def configure(app):
    app.register_blueprint(bp)
