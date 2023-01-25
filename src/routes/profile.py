from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from src.controllers.UserController import UserController

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/', methods=['GET'])
def homepage_html():
    return render_template('homepage.html')


@bp.route('/edit', methods=['GET'])
def update_user_html():
    return render_template('update.html')


@bp.route('/api', methods=['GET'])
@jwt_required()
def homepage():
    identity = get_jwt_identity()
    user = UserController().get_user_by_id(identity)
    return jsonify({'message': 'Welcome to the homepage', 'id': user.get_id(), 'name': user.get_name(),
                    'email': user.get_email(), 'create_at': user.get_created_at()}), 200


@bp.route('/edit', methods=['POST'])
@jwt_required()
def update_user():
    data = request.json
    data['id'] = get_jwt_identity()
    res = UserController().update_user_by_id(data)
    return jsonify({'message': res}), 200


def configure(app):
    app.register_blueprint(bp)
