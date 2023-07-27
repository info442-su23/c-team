import aioboto3

ACCESS_ID = 'XXXXXXX'
SECRET_KEY = 'XXXXXXX'

# Initiate session
async def create_client():
    session = aioboto3.Session()
    async with session.client('s3',
                              region_name='nyc3',
                              endpoint_url='https://nyc3.digitaloceanspaces.com',
                              aws_access_key_id=ACCESS_ID,
                              aws_secret_access_key=SECRET_KEY) as client:
        return client

async def upload_to_s3(lecture_id, material_id, data, mime):
    s3 = await create_client()

    # Your bucket name
    bucket_name = 'lectern-ai-files'

    # The name of the file in the S3 bucket will be the UUID
    key = f"{lecture_id}-{material_id}-{mime}"

    await s3.put_object(Body=data, Bucket=bucket_name, Key=key)

    return key

async def download_from_s3(key):
    s3 = await create_client()

    # Your bucket name
    bucket_name = 'lectern-ai-files'

    response = await s3.get_object(Bucket=bucket_name, Key=key)

    # The object data
    data = response['Body'].read()

    return data
