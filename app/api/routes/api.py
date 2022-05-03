from app.api.routes.endpoints.auth import router as auth
from fastapi import APIRouter

api = APIRouter()
api.include_router(auth, prefix='/auth', tags=['Auth'])
