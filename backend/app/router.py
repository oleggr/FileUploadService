import re

from starlette.responses import JSONResponse, FileResponse
from fastapi import APIRouter, status, UploadFile, File, Request

from app.storage import Storage
from app.logger import logger
from app.notifications import notificator


router = APIRouter()
storage = Storage()


def get_real_ip(headers):
    addr = ''

    if 'x-real-ip' in headers:
        addr = headers['x-real-ip']

    if 'x-forwarded-for' in headers and not addr:
        addr = headers['x-forwarded-for']

    return addr


@router.get(
    "/",
    name='home_page',
    status_code=status.HTTP_200_OK
)
async def main(request: Request):
    addr = get_real_ip(request.headers)
    logger.info(f'Get request: client {addr}')
    return FileResponse('html/index.html')


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(request: Request, request_id: str, file: UploadFile = File(...)):
    addr = get_real_ip(request.headers)

    if not request_id or request_id == '' or request_id == "null":
        logger.alert(f'Failed request - Empty request_id: client {addr}')
        return JSONResponse(
            'Empty request_id',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    if re.match(".*exe", file.filename):
        logger.alert(f'Failed request - Wrong file format: client {addr}')
        return JSONResponse(
            'Wrong file format',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    logger.info(f'File "{file.filename}" for request "{request_id}" uploading started: client {addr}')

    upload_status = storage.put(
        request_id=request_id,
        filename=file.filename,
        data=file.file,
    )

    if upload_status is False:
        return JSONResponse(
            'Upload failed',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return {"file": file.filename}


@router.post(
    "/finish_upload",
    name='finish_file_upload_message',
    status_code=status.HTTP_200_OK
)
async def finish_upload(request: Request, request_id: str):
    request = await request.json()
    notificator.send_success_email(request_id, request['files'])


@router.get(
    "/hello",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def hello():
    return "Hello, world!"
