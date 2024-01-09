from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/signup")
def register():
    return "<p>Signup</p>"


@auth.route("/login")
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"
