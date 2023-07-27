import uuid
import jwt
from aiohttp import web

# from db.file_store import upload_to_s3

routes = web.RouteTableDef()

JWT_SECRET = "fdshlkdfjsdlkvxuv9&^*&v68yvsdyvdsbvsd"

# Happy path flow
# 1. Create subject
# 2. create lecture
# 3. Upload file
# ...
# 4. Summarize
# 5. Get Summary

# Angry path flow
# 1. Delete lecture file
# 2. Delete lecture
# 3. Delete subject

def parse_jwt(request):
    jwt_token = request.cookies.get('my-vouch-ct', None)
    if not jwt_token:
        return web.json_response({'error': 'No JWT provided'}, status=400)
    try:
        # Decode the JWT - replace 'your_secret_key' with your actual secret key
        payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=['HS256'], audience="lectern.ai")
        return payload
    except jwt.PyJWTError as e:
        raise e

@routes.get('/health')
async def health_check(request):
    return web.json_response({"status": "ok", "headers": dict(request.headers)})

@routes.get('/jwt-test')
async def jwt_test(request):
    try:
        payload = parse_jwt(request)
    except jwt.PyJWTError as e:
        return web.json_response({'message': 'Invalid JWT', 'error': e}, status=400)

    return web.json_response(payload)


# SUBJECT

@routes.post('/subject')
async def create_subject(request):
    return web.json_response({"status": "ok"})

@routes.get('/subject')
async def list_subjects(request):
    return web.json_response({ "subjects": [
        {
            "subject_id": "mycoolid",
            "subject_name": "Spanish 102"
        },
        {
            "subject_id": "mycoolid2",
            "subject_name": "Downfall of Mankind 101"
        }
    ]
  })

@routes.get('/subject/{subject_id}')
async def get_subject(request):
    return web.json_response({"status": "ok"})

@routes.delete('/subject/{subject_id}')
async def delete_subject(request):
    return web.json_response({"status": "ok"})

# LECTURE

@routes.post('/subject/lecture')
# Add a lecture to a subject
async def create_lecture(request):
    return web.json_response({"status": "ok"})

@routes.get('/subject/lecture/{lecture_id}')
async def get_lecture(request):
    return web.json_response({"status": "ok"})

@routes.delete('/subject/lecture/{lecture_id}')
async def delete_lecture(request):
    return web.json_response({"status": "ok"})

# MATERIAL

@routes.delete('/subject/lecture/{lecture_id}/{upload_id}')
async def delete_lecture_upload(request):
    return web.json_response({"status": "ok"})

@routes.post('/subject/lecture/{lecture_id}/upload')
# Add a file to a lecture
async def upload_material(request):
    accepted_mime_types = {'audio/mpeg', 'audio/ogg', 'audio/wav'}

    if 'Content-Type' in request.headers:
        content_type = request.headers['Content-Type']

        if content_type not in accepted_mime_types:
            return web.json_response({
                "error": "Unsupported media type."
            }, status=415)

        data = await request.read()
        lecture_id = request.match_info['lecture_id']
        material_id = uuid.uuid4()

        # key = upload_to_s3(lecture_id, material_id, data, content_type.replace('/', '-'))
        key = ""

        # TODO save key in some lecture/subject DB

        return web.json_response({
            "material_id": str(material_id),
            "key": key
        })

    else:
        return web.json_response({
            "error": "Bad request. 'Content-Type' header is missing."
        }, status=400)


# USER SETTINGS


# =============

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print("Fuck it we ball.")
    web.run_app(app)

