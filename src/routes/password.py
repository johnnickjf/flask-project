from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.controllers.PasswordGenerator import PasswordGenerator

bp = Blueprint('password', __name__, url_prefix='/api/password')


@bp.route('/', methods=['POST'])
@jwt_required()
def generate():
    password = PasswordGenerator(request.json)
    return jsonify(password.password_generator())


def configure(app):
    app.register_blueprint(bp)
