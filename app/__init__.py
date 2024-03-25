from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"


def create_app(config_class=Config):
    """Factory function to create the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    from app.auth.routes import bp as auth_bp

    app.register_blueprint(auth_bp)

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
