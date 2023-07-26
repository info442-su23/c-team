from flask import Flask
from myapp.api.uploads import files_blueprint
from flask_uploads import UploadSet, configure_uploads, AllExcept, patch_request_class

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(files_blueprint)

    files = UploadSet('files', AllExcept(('.jpg', '.png', '.gif')))

    configure_uploads(app, files)
    patch_request_class(app)  # set maximum file size, default is 16MB

    return app