from fastapi import APIRouter

from api.routes.endpoints.auth import router as auth

api = APIRouter()
api.include_router(auth, prefix='/auth', tags=['Auth'])
