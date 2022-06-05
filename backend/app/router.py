import re

from starlette.responses import JSONResponse, FileResponse
from fastapi import APIRouter, status, UploadFile, File, Request

from app.storage import Storage
from app.logger import logger


router = APIRouter()
storage = Storage()


@router.get(
    "/",
    name='home_page',
    status_code=status.HTTP_200_OK
)
async def main(request: Request):
    client = request.client
    logger.info(f'Get request: client {client.host} on port {client.port}')
    return FileResponse('html/index.html')


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(request: Request, request_id: str, file: UploadFile = File(...)):
    client = request.client

    if not request_id or request_id == '' or request_id == "null":
        logger.alert(f'Failed request - Empty request_id: client {client.host} on port {client.port}')
        return JSONResponse(
            'Empty request_id',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    if re.match(".*exe", file.filename):
        logger.alert(f'Failed request - Wrong file format: client {client.host} on port {client.port}')
        return JSONResponse(
            'Wrong file format',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    logger.info(f'File "{file.filename}" for request "{request_id}" uploading started: client {client.host} on port {client.port}')

    storage.put(
        request_id=request_id,
        filename=file.filename,
        data=file.file,
    )

    return {"file": file.filename}


@router.get(
    "/hello",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def hello():
    return "Hello, world!"
