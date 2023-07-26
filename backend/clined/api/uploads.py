from flask import current_app, request, abort
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from . import bp
import os

class UploadForm(FlaskForm):
    file = FileField(validators=[
        FileRequired(),
    ])

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@bp.route('/upload-video', methods=['GET', 'POST'])
def upload_video():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if allowed_file(file.filename, current_app.config['ALLOWED_VIDEO_EXTENSIONS']):
            filename = secure_filename(file.filename)
            file.save(os.path.join(bp.root_path, '..', 'uploads', 'video', filename))
            return 'File saved as ' + filename
    abort(400, 'Invalid file type')

@bp.route('/upload-audio', methods=['GET', 'POST'])
def upload_audio():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if allowed_file(file.filename, current_app.config['ALLOWED_AUDIO_EXTENSIONS']):
            filename = secure_filename(file.filename)
            file.save(os.path.join(bp.root_path, '..', 'uploads', 'audio', filename))
            return 'File saved as ' + filename
    abort(400, 'Invalid file type')

@bp.route('/upload-text', methods=['GET', 'POST'])
def upload_text():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if allowed_file(file.filename, current_app.config['ALLOWED_TEXT_EXTENSIONS']):
            filename = secure_filename(file.filename)
            file.save(os.path.join(bp.root_path, '..', 'uploads', 'transcripts', filename))
            return 'File saved as ' + filename
    abort(400, 'Invalid file type')