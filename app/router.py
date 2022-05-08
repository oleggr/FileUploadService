import re
from minio import Minio
from fastapi import APIRouter, status, UploadFile
from starlette.responses import JSONResponse


router = APIRouter()
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
async def main():
    pass


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(file: UploadFile, request_id: str):
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
