from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.router import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.mount("/html", StaticFiles(directory="html"), name="html")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()
