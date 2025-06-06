from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from main.models import Base
from pathlib import Path

# Detecta se estamos no Render (ou em produção)
if os.getenv("ENV") != "production":
    # Só carrega o .env local se NÃO estiver em produção
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL não foi definida nas variáveis de ambiente.")

print("DATABASE_URL:", DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Se estiver usando Alembic, deixe essa linha comentada.
# Base.metadata.create_all(engine)

def criar_sessao():
    return SessionLocal()

# Teste de conexão
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Conexão bem-sucedida:", result.scalar())
except Exception as e:
    print("❌ Erro ao conectar:", e)
