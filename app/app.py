
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import api
from app.core.settings import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
)

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api, prefix=settings.API_PREFIX)



