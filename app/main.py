
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import api
from core.settings import settings

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

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.RELOAD, log_level="info", workers=1, use_colors=True)



