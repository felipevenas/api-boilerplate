from app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False) 
    birth = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)