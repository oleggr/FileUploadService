from minio import Minio
from fastapi import APIRouter, status, UploadFile


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


@router.post(
    "/upload",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def upload(file: UploadFile):
    client.put_object(
        bucket_name='test',
        object_name=file.filename,
        data=file.file,
        length=-1,
        part_size=10485760,
    )

    return {"filename": file.filename}
