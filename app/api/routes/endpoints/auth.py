from datetime import timedelta

from app.api.dependencies import get_db
from app.core.schemas.msj import Response
from app.core.schemas.token import Token
from app.core.schemas.user import UserCreate, UserInDBBase, UserLogin
from app.core.security import create_access_token
from app.core.settings import settings
from app.db.services.user import userService
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/sign-up', response_model=UserInDBBase)
def sign_up(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate
):
    user = userService.find_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='Resource already exists'
        )
    return userService.save(db,object=user_in)
    
    

@router.post('/sign-in', response_model=Token)
def sign_in(
    *, db: Session = Depends(get_db),
    user_data: UserLogin
):
    user = userService.find_by_email(db, email=user_data.email)
    if not user:
        raise HTTPException(status_code=400, detail="invalid creadentials")

    if userService.authenticate(db, email=user.email, password=user.password):
        raise HTTPException(status_code=400, detail="invalid creadentials")
    

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token({
            "id": user.id 
        }, 
        expires_delta=access_token_expires),
        "token_type": "bearer",
    }
    