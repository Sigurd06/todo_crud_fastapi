from typing import Optional, TypeVar

from pydantic import BaseModel

T = TypeVar('T')

class Response(BaseModel):
    status: int
    message: str
    data: Optional[T] = None
