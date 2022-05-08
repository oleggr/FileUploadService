import re
from minio import Minio
from starlette.responses import JSONResponse, FileResponse
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, status, UploadFile, Form, File

import config


router = APIRouter()
templates = Jinja2Templates(directory="static")
client = Minio(
    "storage:9000",
    # "127.0.0.1:9000",
    access_key=config.access_key,
    secret_key=config.secret_key,
    secure=False
)


@router.get(
    "/hello",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def hello():
    return "Hello, world!"


@router.get(
    "/upload",
    name='upload_page',
    status_code=status.HTTP_200_OK
)
async def main():
    return FileResponse('html/index.html')


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(file: UploadFile = File(...), request_id: str = Form(...)):
    if re.match(".*exe", file.filename):
        return JSONResponse(
            'Wrong file format',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    client.put_object(
        bucket_name='main',
        object_name=request_id + '_' + file.filename,
        data=file.file,
        length=-1,
        part_size=10485760,
    )

    return {"file": file.filename}
