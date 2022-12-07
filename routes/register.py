from flask import Blueprint, render_template, request

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/', methods=['GET', 'POST'])
def register():
    return "register"


def configure(app):
    app.register_blueprint(bp)
