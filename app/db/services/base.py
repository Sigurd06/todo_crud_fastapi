from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app.db.base_class import Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseSevice(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def find_by_id(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def find_all_with_paginate(self, db: Session,*, skip: int = 0, limit: int = 50) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def save(self, db: Session, *, object: CreateSchemaType) -> ModelType:
        json_data = jsonable_encoder(object)
        object_db = self.model(**json_data)
        db.add(object_db)
        db.commit()
        db.refresh(object_db)
        return object_db

    def update(self, db: Session, *, object_db: ModelType, object: Union[UpdateSchemaType, Dict[str, Any]]):
        json_data = jsonable_encoder(object_db)
        if isinstance(object, dict):
            update_data = object
        else :
            update_data = object.dict(exclude_unset=True)
        
        for field in json_data:
            if field in update_data:
                setattr(object_db, field, update_data[field])
        
        db.add(object_db)
        db.commit()
        db.refresh(object_db)
        return object_db

    def delete(self, db: Session, *, id: int)-> ModelType:
        object = db.query(self.model).get(id)
        db.delete(object)
        db.commit()
        return object
