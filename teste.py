from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:SUA_SENHA@localhost:5432/ci_cd"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro de conexão: {e}")
