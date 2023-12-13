from datetime import datetime

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(limit: int, skip: int, db: Session):
    return db.query(Contact).limit(limit).offset(skip).all()


async def get_contact_by_id(contact_id: int, db: Session):
    return db.query(Contact).filter_by(id=contact_id).first()


async def get_contact_by_email(contact_email: str, db: Session):
    return db.query(Contact).filter_by(email=contact_email).first()


async def get_contact_by_name(contact_name: str, db: Session):
    return db.query(Contact).filter_by(first_name=contact_name).all()


async def get_contact_by_surname(contact_surname: str, db: Session):
    return db.query(Contact).filter_by(surname=contact_surname).all()


async def get_contact_by_phone(phone: str, db: Session):
    return db.query(Contact).filter(Contact.phone_number == phone).first()


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(body: ContactModel, db: Session, contact_id: int):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_birthday_contact(db: Session):
    contacts = db.query(Contact).all()
    contacts_result = []
    today = datetime.now().date()
    for contact in contacts:
        contact_birthday = contact.birthday.replace(year=datetime.now().year)
        maybe_seven_days = (contact_birthday - today).days
        if 0 <= maybe_seven_days <= 7:
            print(maybe_seven_days)
            contacts_result.append(contact)
    return contacts_result
