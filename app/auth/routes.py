from flask import render_template
from flask import Blueprint

bp = Blueprint("auth", __name__)


@bp.route("/")
@bp.route("/login")
def index():
    """
    Render Website Registration Page.
    """
    return render_template("index.html")
