import asyncpg
from sql import *

async def init_db():
    conn = await asyncpg.connect(user='yourusername', password='yourpassword', 
                                 database='yourdatabase', host='localhost')
    for command in INIT_DB:
        await conn.execute(command)
    await conn.close()

async def upload_file_key_to_db(auth_token, lecture_uuid, s3_key):
    conn = await asyncpg.connect(user='yourusername', password='yourpassword', 
                                 database='yourdatabase', host='localhost')
    await conn.execute(UPLOAD_FILE_KEY, auth_token, lecture_uuid, s3_key)
    await conn.close()

async def retrieve_key(auth_token, lecture_uuid):
    conn = await asyncpg.connect(user='yourusername', password='yourpassword', 
                                 database='yourdatabase', host='localhost')
    s3_key = await conn.fetchval('''
        SELECT s3_key FROM s3_keys WHERE auth_token = $1 AND lecture_uuid = $2
    ''', auth_token, lecture_uuid)
    await conn.close()
    return s3_key
