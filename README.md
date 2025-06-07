![CI](https://github.com/ravizeraig/consumo-energia/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-✔️-blue)

# ⚡ Projeto Consumo de Energia — Análise e Notificação

## 📌 Visão Geral

Este projeto realiza o monitoramento do consumo de energia (kWh) por região, a partir de dados armazenados em um banco PostgreSQL. A aplicação realiza análises automáticas e envia alertas por e-mail quando o consumo atinge níveis críticos. Tudo é executado com segurança e automação via Docker e GitHub Actions (CI/CD).

---

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **PostgreSQL** (local ou na nuvem - Render)
- **Docker**
- **GitHub Actions** (CI/CD)
- **SMTP** (envio de e-mails com segurança)
- **SQLAlchemy** (ORM)
- **dotenv** (`.env` para variáveis sensíveis)
- **Jupyter Notebook** (para testes e validações)

---

## 📂 Estrutura de Diretórios

main/
├── db.py # Conexão com banco
├── enviar_email.py # Envio de alertas
├── gerar_relatorio.py # Cálculos e verificações
├── models.py # Tabelas do banco (ORM)
└── main.py # Execução principal
.env.example # Exemplo de variáveis de ambiente
Dockerfile # Build Docker

yaml
Copiar
Editar

---

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/ravizeraig/consumo-energia.git
cd consumo-energia
```
### 2. Configure seu `.env`

Crie um arquivo `.env` com base no `.env.example`:

```env
# Configurações de email
EMAIL_REMETENTE=seu_email@example.com
SENHA_APP=sua_senha_de_app
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465

# Banco de dados
DATABASE_URL=postgresql+psycopg2://usuario:senha@host:porta/nome_do_banco

# Ambiente
ENV=development
````
✅ Para usar o banco no Render, substitua host, porta, usuario, senha e nome_do_banco com os dados fornecidos pelo serviço.

✅ Para usar localmente com Docker Compose, use host=db e porta=5432.

---
## 🐳 Executando com Docker

### 🔧 Build da imagem

```bash
docker build -t consumo-energia .
```
### ▶️ Execução do container com variáveis
```bash
Copiar
Editar
docker run --env-file .env consumo-energia
```
### 🔁 CI/CD com GitHub Actions
A automação do projeto está configurada com:

CI: Testes automáticos e validação do código a cada push

CD: Deploy automatizado para Render.com via Docker

---

### ✉️ Notificações por Email
O envio de alertas é feito via SMTP (ex: Gmail), com segurança reforçada usando senhas de aplicativo. Nenhuma senha é exposta no código.
---
### ☁️ Banco de Dados na Nuvem (Render)
Este projeto está pronto para usar o banco PostgreSQL fornecido pelo Render.
Basta ajustar a DATABASE_URL no .env com as credenciais geradas.
---
### 🧪 Validação e Testes
Os dados e alertas foram validados com:
---
### Consultas SQL via SQLAlchemy

Análises com Pandas e Jupyter Notebook

Simulações com dados fictícios para verificar lógica de alertas

---
### 👨‍💻 Autor
Desenvolvido por Igor de Paula como projeto prático para portfólio DevOps/Data.

---
### 📄 Licença
Este projeto está licenciado sob a MIT License.

Para mais detalhes, consulte o arquivo LICENSE na raiz do repositório.


