from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    cargo_pretendido = Column(String, nullable=False)
    disponibilidade = Column(String, nullable=False)
    status = Column(String, default="ativo")
