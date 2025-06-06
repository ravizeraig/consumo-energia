#!/bin/bash

echo "Ambiente: $ENV"
echo "Banco: $DB_HOST:$DB_PORT"

if [ "$ENV" = "production" ]; then
  echo "Rodando diretamente em produção..."
  exec python -m main.main
else
  echo "Aguardando o banco de dados (modo desenvolvimento)..."
  ./wait-for-it.sh "$DB_HOST" "$DB_PORT" -- python -m main.main
fi
