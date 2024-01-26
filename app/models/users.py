from sqlalchemy import Column, String

from .base import BaseModel


class UserDB(BaseModel):
    __tablename__ = "users"

    username = Column(String)
    password = Column(String)
    salt = Column(String)
    role = Column(String)
