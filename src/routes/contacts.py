from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Query, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactResponse, ContactModel
from src.repository import contacts as repository_contacts


router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def get_contacts(limit: int = Query(default=10, le=50), skip: int = 0, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(limit, skip, db)
    return contacts


@router.get("/search_by_email", response_model=ContactResponse)
async def get_contact_by_email(contact_email: str, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(contact_email, db)
    return contact


@router.get("/search_by_name", response_model=List[ContactResponse])
async def get_contact_by_name(contact_name: str, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_name(contact_name, db)
    return contact


@router.get("/search_by_surname", response_model=List[ContactResponse])
async def get_contact_by_surname(contact_surname: str, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_surname(contact_surname, db)
    return contact


@router.get("/birthday", response_model=List[ContactResponse])
async def get_birthday_contact(db: Session = Depends(get_db)):
    contact = await repository_contacts.get_birthday_contact(db)
    return contact


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact_by_id(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_phone(body.phone_number, db)
    print(contact)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Contact with this number already exists!")
    contact = await repository_contacts.create_contact(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(body, db, contact_id)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact
