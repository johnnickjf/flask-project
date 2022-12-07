from flask import Blueprint, render_template, request

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    return "login"


def configure(app):
    app.register_blueprint(bp)
