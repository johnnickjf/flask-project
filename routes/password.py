from flask import Blueprint, render_template, request, jsonify
from src.Controllers.PasswordGenerator import PasswordGenerator

bp = Blueprint('password', __name__, url_prefix='/api/password')


@bp.route('/', methods=['GET', 'POST'])
def register():
    password = PasswordGenerator(request.args)
    return jsonify(password.password_generator())


def configure(app):
    app.register_blueprint(bp)
