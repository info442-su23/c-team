from flask import Flask
from .api import bp as api_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
