from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.controllers.password_generator import PasswordGenerator

bp = Blueprint('password', __name__, url_prefix='/api/password')


@bp.route('/', methods=['POST'])
@jwt_required()
def generate():
    password = PasswordGenerator(request.json)
    return jsonify({'password': password.password_generator()},
                   {'message': 'Password generated successfully'}), 200


def configure(app):
    app.register_blueprint(bp)
