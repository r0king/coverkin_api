from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from .database import Base




class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    items = relationship("Sheet", back_populates="owner", uselist=False)



class Sheet(Base):

    __tablename__ = "items"


    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    owner_id = Column(String, ForeignKey("users.email"))

    owner = relationship("User", back_populates="items")