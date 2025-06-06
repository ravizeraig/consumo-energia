# Usar uma imagem oficial do Python
FROM python:3.11

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . .

# Instalar netcat para o wait-for-it funcionar
RUN apt-get update && apt-get install -y netcat-openbsd

# Dar permissão de execução aos scripts
RUN chmod +x /app/wait-for-it.sh
RUN chmod +x /app/entrypoint.sh

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão
CMD ["./entrypoint.sh"]


