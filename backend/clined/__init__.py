from flask import Flask
from flask_cors import CORS
from .api import bp as api_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    # TODO Make this an .env variable
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(api_bp, url_prefix="/api")

    return app