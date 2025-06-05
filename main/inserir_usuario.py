# main/inserir_usuario.py

from main.db import criar_sessao
from main.usuarios import inserir_usuario

if __name__ == "__main__":
    with criar_sessao() as sessao:
        inserir_usuario(sessao, nome="Igor de Paula", email="igor.diipaula@gmail.com", empresa="MinhaEmpresa", regiao="Sul")

