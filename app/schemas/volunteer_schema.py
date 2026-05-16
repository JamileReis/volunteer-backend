from pydantic import BaseModel

class VolunteerBase(BaseModel):
    nome: str
    email: str
    telefone: str
    cargo_pretendido: str
    disponibilidade: str
    status: str

class VolunteerCreate(VolunteerBase):
    pass

class VolunteerResponse(VolunteerBase):
    id: int

    class Config:
        from_attributes = True
