from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    status = Column(String, default="new")
    next_follow_up = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
