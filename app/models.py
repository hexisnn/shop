from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    
    