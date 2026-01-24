from pydantic import BaseModel, ConfigDict
from datetime import datetime, date

class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    birth: date

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    active: bool
    created_at: datetime
    updated_at: datetime

class UserUpdate(UserBase):
    active: bool
