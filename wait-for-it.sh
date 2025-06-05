#!/usr/bin/env bash
set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  echo "🕒 Aguardando o banco de dados ($host:$port)..."
  sleep 2
done

>&2 echo "✅ Banco de dados está disponível — executando o app!"
exec $cmd

