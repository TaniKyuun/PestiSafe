from flask import render_template
from flask import Blueprint

bp = Blueprint("auth", __name__)


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")
