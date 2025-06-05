# main/db.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from main.models import Base

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL:", DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)  # echo=True ajuda a depurar
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base.metadata.create_all(engine)

def criar_sessao():
    return SessionLocal()

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))  # Correção aqui
        print("Conexão bem-sucedida:", result.scalar())
except Exception as e:
    print("Erro ao conectar:", e)
