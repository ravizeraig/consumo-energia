# main/usuarios.py

from sqlalchemy.orm import Session
from models import Usuario

def inserir_usuario(session: Session, nome: str, email: str, empresa: str, regiao: str):
    novo_usuario = Usuario(nome=nome, email=email, empresa=empresa, regiao=regiao)
    session.add(novo_usuario)
    session.commit()
    print(f"✅ Usuário {nome} inserido com sucesso!")