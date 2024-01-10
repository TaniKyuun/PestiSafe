from flask import Blueprint, render_template
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)


@views.route("/login")
def login():
    return render_template("login.html", user=current_user)


@views.route("/result")
@login_required
def results():
    return render_template("result.html", user=current_user)


@views.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/submit_sample", methods=["GET", "POST"])
@login_required
def submit_sample():
    return render_template("submit_sample.html", user=current_user)
