from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ARRAY


Base = declarative_base()

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255), unique=True)
    address = Column(String(255))
    role = Column(ARRAY(String(255)))
    create_at = Column(Date()) 

    
    