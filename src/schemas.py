from datetime import date
from pydantic import BaseModel, EmailStr


class ContactModel(BaseModel):
    first_name: str
    surname: str
    email: EmailStr
    phone_number: str
    birthday: date


class ContactResponse(ContactModel):
    id: int = 1

    class Config:
        orm_mode = True
