from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
  # user submits form
  if request.method == "GET":
    email = request.form.get("email")
    password = request.form.get("password1")

    if len(email) < 1:
      flash(
        "Email field is required. Please enter your email address.",
        category="error",
      )
    elif len(password) < 1:
      flash(
        "Password field is required. Please enter your password.",
        category="error",
      )
    else:
      # check if user exists
      user = User.query.filter_by(email=email).first()
      if user and check_password_hash(user.password, password):
        flash("Logged in successfully!", category="success")
        login_user(user, remember=True)
        return redirect(url_for("views.dashboard"))
      flash("Incorrect email or password, please try again.", category="error")

  return render_template("login.html", user=current_user)


@auth.route("/sign-up", methods=["POST"])
def sign_up():
  # user submits form
  if request.method == "POST":
    email = request.form.get("email")
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    user = User.query.filter_by(email=email).first()
    # flash messages
    if user:
      flash("Email already exists.", category="error")
    elif len(email) < 4:
      flash("Email must be greater than 3 characters.", category="error")
    elif len(first_name) < 2:
      flash("First name must be greater than 1 character.", category="error")
    elif len(last_name) < 2:
      flash("Last name must be greater than 1 character.", category="error")
    elif password1 != password2:
      flash("Passwords don't match.", category="error")
    elif len(password1) < 7:
      flash("Password must be at least 7 characters.", category="error")
    else:
      # add user to database
      new_user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_active=True,
        password=generate_password_hash(password1, method="pbkdf2:sha256"),
      )
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)  # Use new_user instead of user
      flash("Account created!", category="success")
      return redirect(url_for("views.dashboard"))

  return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("auth.login"))
