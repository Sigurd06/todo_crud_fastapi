from typing import Any, Dict, Optional, Union

from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from app.db.services.base import BaseSevice
from sqlalchemy.orm import Session


class UserService(BaseSevice[User, UserCreate, UserUpdate]):
    def find_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def save(self, db: Session, *, object: UserCreate) -> User:
        object_db = User(
            email=object.email,
            username=object.username,
            password=get_password_hash(object.password),
        )
        db.add(object_db)
        db.commit()
        db.refresh(object_db)
        return object_db

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.find_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

userService = UserService(User)
