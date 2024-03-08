from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Add a new column to the Results table called 'user_id' to the User table
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    is_active = db.Column(db.Boolean, default=True)
    password = db.Column(db.String(150))
    results = db.relationship("Results")
    # Add a new column to the User table called 'posts' to the Post table
