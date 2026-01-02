from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from database import get_db, engine
from models import Lead, Base
from datetime import datetime

Base.metadata.create_all(bind=engine)

router = APIRouter()

class LeadCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None
    status: str | None = "new"
    next_follow_up: date | None = None

@router.post("/")
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/")
def get_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()

@router.get("/{lead_id}")
def get_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    db.delete(lead)
    db.commit()
    return {"message": "Lead deleted"}

@router.put("/{lead_id}/status")
def update_status(lead_id: int, status: str, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = status
    lead.last_contacted = datetime.utcnow()
    db.commit()

    return {"message": "Lead status updated"}


@router.get("/followups/today")
def todays_followups(db: Session = Depends(get_db)):
    today = date.today()
    leads = db.query(Lead).filter(
        Lead.next_follow_up == today,
        Lead.status != "closed"
    ).all()
    return leads


