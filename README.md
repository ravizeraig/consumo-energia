# Projeto Consumo de Energia — Análise e Notificação

## Introdução

Este projeto tem como objetivo monitorar o consumo de energia (kWh) por regiões a partir de um banco de dados criado para teste. O sistema lê os dados, realiza somatórios, verifica o consumo, e envia notificações por email para usuários cadastrados. O foco principal é aplicar boas práticas de segurança, integração contínua e deploy usando Docker.

---

## Tecnologias e Ferramentas

- Python 3.x  
- Banco de dados: PostgreSQL para armazenamento dos dados  
- Docker para containerização  
- Variáveis de ambiente com `.env` para segurança  
- Jupyter Notebook para validação e análise dos dados  
- SMTP para envio seguro de emails, evitando exposição de senhas

---

## Como foi construído

1. **Criação dos dados:** Geração de dados de consumo de energia para diferentes regiões, inseridos em uma tabela PostgreSQL para simulação.  
2. **Configuração do banco:** Tabela criada com esquema para armazenar dados e cadastro de usuários para envio de emails.  
3. **Validação e análise:** Uso de Jupyter Notebook para validar os dados e garantir integridade.  
4. **Lógica do projeto:**  
   - Leitura dos dados do banco  
   - Cálculo do consumo total por região  
   - Verificação de limites/alertas de consumo  
   - Consulta dos usuários cadastrados para notificações  
5. **Envio de email:** Integração com servidor SMTP, utilizando variáveis de ambiente para credenciais, garantindo segurança.  
6. **Containerização:** Dockerfile criado para build e deploy do projeto, facilitando distribuição e execução.  
7. **CI/CD (em andamento):** Planejado para automação de testes e deploy em ambiente controlado.

---

## Como usar

1. Clone o repositório  
2. Crie e configure o arquivo `.env` com as variáveis necessárias (exemplo: credenciais SMTP, conexão com PostgreSQL)  
3. Execute o container Docker:  
   ```bash
   docker build -t cd-app .
   docker run --env-file .env cd-app
