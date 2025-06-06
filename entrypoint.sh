#!/bin/bash

echo "Ambiente: $ENV"

if [ "$ENV" = "production" ]; then
  echo "Rodando diretamente em produção..."
  exec python -m main.main
else
  echo "Aguardando o banco de dados (modo desenvolvimento)..."
  ./wait-for-it.sh db 5432 -- python -m main.main
fi
