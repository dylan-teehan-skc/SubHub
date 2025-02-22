from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from typing import Optional

class User(Base):
    address = Column(String, nullable=True)
    location = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    card_holder_id = Column(String, nullable=True)

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    real_card_id = Column(Integer, ForeignKey('real_cards.id'), unique=True)

    real_card = relationship("RealCard", back_populates="user", uselist=False)
    groups = relationship("Group", back_populates="admin")
    card_memberships = relationship("CardMember", back_populates="user")