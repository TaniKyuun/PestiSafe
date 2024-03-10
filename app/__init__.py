from flask import Flask
from config import Config


def create_app(config_class=Config):
    """Factory function to create the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.auth.routes import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
