from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import DateTime, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    surname = Column(String(30))
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True, nullable=False)
    birthday = Column(Date)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
