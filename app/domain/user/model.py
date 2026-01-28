from app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    phone = Column(String(15), nullable=False)
    birth = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)