import os
import unittest
from werkzeug import FileStorage
from clined import create_app

class UploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
    
    def tearDown(self):
        self.app_context.pop()

    def test_upload_video(self):
        with open('tests/test_files/test.mp4', 'rb') as f:
            data = {
                'video': FileStorage(
                    stream=f,
                    filename='test.mp4',
                    content_type='video/mp4',
                )
            }
            response = self.client.post('/upload-video', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)

    def test_upload_audio(self):
        with open('tests/test_files/test.mp3', 'rb') as f:
            data = {
                'audio': FileStorage(
                stream=f,
                filename='test.mp3',
                content_type='audio/mpeg',
                )
            }
            response = self.client.post('/upload-audio', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            self.assertIn('File saved', response.data.decode())

    def test_upload_text(self):
        with open('tests/test_files/test.txt', 'rb') as f:
            data = {
                'text': FileStorage(
                stream=f,
                filename='test.txt',
                content_type='text/plain',
                )
            }
            response = self.client.post('/upload-text', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            self.assertIn('File saved', response.data.decode())

    def test_upload_wrong_format(self):
        with open('tests/test_files/test.jpg', 'rb') as f:
            data = {
                'video': FileStorage(
                    stream=f,
                    filename='test.jpg',
                    content_type='image/jpeg',
                )
            }
            response = self.client.post('/upload-video', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 400)  # change this to the status code your app returns for an invalid file format

if __name__ == '__main__':
    unittest.main()