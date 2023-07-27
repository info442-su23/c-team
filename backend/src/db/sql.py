#A file for storing SQL comands

INIT_FILE_KEY_TABLE = '''
        CREATE TABLE IF NOT EXISTS s3_keys (
            auth_token TEXT NOT NULL,
            lecture_uuid UUID NOT NULL,
            s3_key TEXT NOT NULL
        );
    '''

INIT_DB = [INIT_FILE_KEY_TABLE]

UPLOAD_FILE_KEY = '''
        INSERT INTO s3_keys (auth_token, lecture_uuid, s3_key) VALUES ($1, $2, $3)
    '''