from flask import Blueprint, render_template

mod = Blueprint('article', __name__)


@mod.route('/article')
def index():
    return render_template('article/index.html')
