from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
import aiofiles
import os
import asyncio
import glob
from big_chungus import split_text_into_chunks
from agents import label, summarize, table_of_contents
from utils.file_converters import *
from utils.speech_2_text import *

app = FastAPI()

VIDEO_UPLOAD_FOLDER = '/path/to/the/video/uploads'
AUDIO_UPLOAD_FOLDER = '/path/to/the/audio/uploads'
TRANSCRIPT_FOLDER = "string"
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv'}
ALLOWED_AUDIO_EXTENSIONS = {'mp3', 'wav'}

class FileUploadResponse(BaseModel):
    detail: str

async def process_transcript(file):
    async with aiofiles.open(file, 'r') as f:
        text = await f.read()
        chunks = split_text_into_chunks(text)
        labels = await label(chunks)
        table = await table_of_contents(labels)
        summary = await summarize(chunks)
        
        return json.dumps({
            'file': file,
            'text': text,
            'chunks': chunks,
            'labels': labels,
            'table': table,
            'summary': summary
            })

async def process_all_transcripts():
    files = glob.glob(os.path.join(TRANSCRIPT_FOLDER, '*.txt'))
    tasks = [process_transcript(file) for file in files]

    return json.dumps({
        'list': await asyncio.gather(*tasks)
    })

async def save_file(file: UploadFile, folder: str):
    async with aiofiles.open(os.path.join(folder, file.filename), 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write

async def process_file(filename: str, folder: str):
    if(folder == VIDEO_UPLOAD_FOLDER):
        extract_audio_from_video(VIDEO_UPLOAD_FOLDER, AUDIO_UPLOAD_FOLDER)
    await transcribe_directory(AUDIO_UPLOAD_FOLDER, TRANSCRIPT_FOLDER)
    # Include here your logic to process the file
    await asyncio.sleep(1)  # Just an example of an async operation
    print(f"Processed file: {filename}")

@app.post("/upload/", response_model=FileUploadResponse)
async def upload_file(file: UploadFile):
    ext = file.filename.split('.')[-1]
    if ext in ALLOWED_VIDEO_EXTENSIONS:
        upload_folder = VIDEO_UPLOAD_FOLDER
    elif ext in ALLOWED_AUDIO_EXTENSIONS:
        upload_folder = AUDIO_UPLOAD_FOLDER
    else:
        raise HTTPException(status_code=400, detail="Invalid file type")

    await save_file(file, upload_folder)  # Save the file first
    asyncio.create_task(process_file(file.filename, upload_folder))  # async task for processing file
    return {"detail": f"Successfully uploaded and processing {file.filename}"}
