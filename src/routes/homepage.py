from flask import Blueprint, render_template, request

bp = Blueprint('homepage', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


def configure(app):
    app.register_blueprint(bp)
