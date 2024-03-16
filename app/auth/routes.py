from flask import render_template, flash, redirect
from flask import Blueprint
from app.auth.forms import LoginForm

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect("/index")
    return render_template("auth/login.html", title="Sign In", form=form)
