import re
from minio import Minio
from fastapi import APIRouter, status, UploadFile, Request
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="static")
client = Minio(
    "storage:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
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
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(file: UploadFile, request_id: str = 'tmp-prefix'):
    if re.match(".*exe", file.filename):
        return JSONResponse(
            'Wrong file format',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    client.put_object(
        bucket_name='test',
        object_name=request_id + '_' + file.filename,
        data=file.file,
        length=-1,
        part_size=10485760,
    )

    return {"filename": file.filename}
