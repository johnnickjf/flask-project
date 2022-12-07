from flask import Blueprint, request, jsonify
from src.Controllers.PasswordGenerator import PasswordGenerator

bp = Blueprint('password', __name__, url_prefix='/api/password')


@bp.route('/', methods=['POST', 'GET'])
def generate():
    if request.method == 'POST':
        password = PasswordGenerator(request.form)
        return jsonify(password.password_generator())
    else:
        password = PasswordGenerator(request.args)
        return jsonify(password.password_generator())


def configure(app):
    app.register_blueprint(bp)
