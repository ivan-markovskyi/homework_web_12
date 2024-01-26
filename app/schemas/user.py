import enum
from pydantic import BaseModel


class RolesEnum(str, enum.Enum):
    USER = "user"
    MANAGER = "manager"
    ADMIN = "ADMIN"


class User(BaseModel):
    id: int
    username: str
    password: str
    role: RolesEnum

    class Config:
        from_attributes = True
