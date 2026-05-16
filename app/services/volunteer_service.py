
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.volunteer_model import Volunteer
from app.schemas.volunteer_schema import VolunteerCreate

class VolunteerService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Volunteer).all()

    @staticmethod
    def create(db: Session, payload: VolunteerCreate):
        exists = db.query(Volunteer).filter(
            Volunteer.email == payload.email
        ).first()

        if exists:
            raise HTTPException(
                status_code=409,
                detail="Email já cadastrado"
            )

        volunteer = Volunteer(**payload.model_dump())

        db.add(volunteer)
        db.commit()
        db.refresh(volunteer)

        return volunteer

    @staticmethod
    def update(
        db: Session,
        volunteer_id: int,
        payload: VolunteerCreate
    ):
        volunteer = db.query(Volunteer).filter(
            Volunteer.id == volunteer_id
        ).first()

        if not volunteer:
            raise HTTPException(
                status_code=404,
                detail="Voluntário não encontrado"
            )

        for key, value in payload.model_dump().items():
            setattr(volunteer, key, value)

        db.commit()
        db.refresh(volunteer)

        return volunteer

    @staticmethod
    def delete(db: Session, volunteer_id: int):
        volunteer = db.query(Volunteer).filter(
            Volunteer.id == volunteer_id
        ).first()

        if not volunteer:
            raise HTTPException(
                status_code=404,
                detail="Voluntário não encontrado"
            )

        volunteer.status = "inativo"

        db.commit()

        return {"message": "Voluntário inativado"}
