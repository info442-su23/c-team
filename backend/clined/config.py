class Config:
    SECRET_KEY = 'your-secret-key'
    UPLOADS = 'myapp/uploads'
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv'}
    ALLOWED_AUDIO_EXTENSIONS = {'mp3', 'mp4a', 'm4p', 'raw', 'wav'}
    ALLOWED_TEXT_EXTENSIONS = {'pdf', 'docx', 'rtf', 'txt'}
    WTF_CSRF_ENABLED = False
    # In bytes
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024 * 1024
    #TODO Fix CORS bs
    #WTF_CSRF_CHECK_DEFAULT = False
    #WTF_CSRF_HEADERS = ['X-Csrf-Token']