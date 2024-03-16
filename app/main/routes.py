from flask import render_template
from flask import Blueprint

bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/index")
def index():
    """Render Website Landing Page."""
    return render_template("index.html")
