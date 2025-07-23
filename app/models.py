from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: Optional[int] = Field(None, ge=0)
