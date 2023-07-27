import os
import pytest
from werkzeug.datastructures import FileStorage
from clined import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app

def test_upload_video(app, client):
    with app.app_context():
        # Correct format file
        data = {
            'file': (open('clined/tests/test_files/test.mp4', 'rb'), 'test.mp4')
        }
        response = client.post('/api/upload-video', content_type='multipart/form-data', data=data)
        assert response.status_code == 200

        # Incorrect format file
        data = {
            'file': (open('clined/tests/test_files/test.txt', 'rb'), 'test.txt')
        }
        response = client.post('/api/upload-video', content_type='multipart/form-data', data=data)
        assert response.status_code == 400

def test_upload_audio(app, client):
    with app.app_context():
        # Correct format file
        data = {
            'file': (open('clined/tests/test_files/test.mp3', 'rb'), 'test.mp3')
        }
        response = client.post('/api/upload-audio', content_type='multipart/form-data', data=data)
        assert response.status_code == 200

        # Incorrect format file
        data = {
            'file': (open('clined/tests/test_files/test.txt', 'rb'), 'test.txt')
        }
        response = client.post('/api/upload-audio', content_type='multipart/form-data', data=data)
        assert response.status_code == 400

def test_upload_text(app, client):
    with app.app_context():
        # Correct format file
        data = {
            'file': (open('clined/tests/test_files/test.txt', 'rb'), 'test.txt')
        }
        response = client.post('/api/upload-text', content_type='multipart/form-data', data=data)
        assert response.status_code == 200

        # Incorrect format file
        data = {
            'file': (open('clined/tests/test_files/test.mp3', 'rb'), 'test.mp3')
        }
        response = client.post('/api/upload-text', content_type='multipart/form-data', data=data)
        assert response.status_code == 400