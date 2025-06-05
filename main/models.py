from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    empresa = Column(String(100), nullable=False)
    regiao = Column(String(100), nullable=False)

    def __repr__(self):
        return (
            f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', "
            f"empresa='{self.empresa}', regiao='{self.regiao}')>"
        )
