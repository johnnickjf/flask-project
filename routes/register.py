from flask import Blueprint, render_template, request
from src.dao.UserDao import UserDao

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/', methods=['POST'])
def register():



def configure(app):
    app.register_blueprint(bp)
