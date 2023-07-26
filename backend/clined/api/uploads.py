from flask import Blueprint, request
from flask_uploads import UploadSet

files_blueprint = Blueprint('files', __name__)
files = UploadSet('files')

@files_blueprint.route('/upload-video', methods=['POST'])
def upload_video():
    filename = files.save(request.files['video'], folder='video')
    return 'File saved as ' + filename

@files_blueprint.route('/upload-audio', methods=['POST'])
def upload_audio():
    filename = files.save(request.files['audio'], folder='audio')
    return 'File saved as ' + filename

@files_blueprint.route('/upload-text', methods=['POST'])
def upload_text():
    filename = files.save(request.files['text'], folder='transcripts')
    return 'File saved as ' + filename