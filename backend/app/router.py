import re
from starlette.responses import JSONResponse, FileResponse
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, status, UploadFile, File

from app.storage import Storage


router = APIRouter()
templates = Jinja2Templates(directory="static")
storage = Storage()


@router.get(
    "/",
    name='home_page',
    status_code=status.HTTP_200_OK
)
async def main():
    return FileResponse('html/index.html')


@router.post(
    "/upload",
    name='upload_file',
    status_code=status.HTTP_200_OK
)
async def upload(request_id: str, file: UploadFile = File(...)):
    if re.match(".*exe", file.filename):
        return JSONResponse(
            'Wrong file format',
            status_code=status.HTTP_400_BAD_REQUEST,
        )

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
