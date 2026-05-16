from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.volunteer_schema import (
    VolunteerCreate,
    VolunteerResponse
)
from app.services.volunteer_service import VolunteerService

router = APIRouter(prefix="/voluntarios", tags=["Voluntarios"])

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[VolunteerResponse])
def get_volunteers(db: Session = Depends(get_db)):
    return VolunteerService.get_all(db)

@router.post("", response_model=VolunteerResponse)
def create_volunteer(
    payload: VolunteerCreate,
    db: Session = Depends(get_db)
):
    return VolunteerService.create(db, payload)

@router.put("/{volunteer_id}")
def update_volunteer(
    volunteer_id: int,
    payload: VolunteerCreate,
    db: Session = Depends(get_db)
):
    return VolunteerService.update(
        db,
        volunteer_id,
        payload
    )

@router.delete("/{volunteer_id}")
def delete_volunteer(
    volunteer_id: int,
    db: Session = Depends(get_db)
):
    return VolunteerService.delete(db, volunteer_id)