from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, date


class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    description: str | None

    @validator("birthday", pre=True)
    def string_to_date(cls, v: object) -> object:
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d").date()
        return v

    class Config:
        from_attributes = True


class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    description: str | None


class ContactUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone_number: str | None
    birthday: date | None
    description: str | None
