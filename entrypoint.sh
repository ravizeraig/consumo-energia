#!/bin/bash
set -e

echo "===== INICIANDO O ENTRYPOINT ====="
echo "Ambiente: $ENV"
echo "Banco: $DB_HOST:$DB_PORT"

if [ -z "$DB_HOST" ] || [ -z "$DB_PORT" ]; then
  echo "❌ Variáveis DB_HOST ou DB_PORT não definidas!"
  exit 1
fi

if [ "$ENV" = "production" ]; then
  echo "Rodando diretamente em produção..."
  exec python -m main.main
else
  echo "Aguardando o banco de dados (modo desenvolvimento)..."
  ./wait-for-it.sh "$DB_HOST" "$DB_PORT" --timeout=30 --strict -- echo "✅ Banco disponível, iniciando app..." && exec python -m main.main
fi
