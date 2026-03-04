from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime, date
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    username: str
    phone: str
    birth: date

class UserCreate(UserBase):
    username: str
    password: str
    pass

class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    active: bool
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    birth: Optional[date] = None
    active: Optional[bool] = None

