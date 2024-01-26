from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import BaseModel, Base


class ContactDB(BaseModel):
    __tablename__ = "contacts"

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birthday = Column(String)
    description = Column(String)

    user_id = Column(ForeignKey("users.id"), nullable=True)
    user = relationship("UserDB", backref="users", lazy="joined")
