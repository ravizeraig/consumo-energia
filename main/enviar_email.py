import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
import os
from main.db import criar_sessao # Função que retorna a sessão SQLAlchemy


# Carregar variáveis do .env
load_dotenv()

def enviar_relatorio():
    from main.models import Usuario  # Import interno para evitar import circular

    # Variáveis de ambiente
    email_remetente = os.getenv('EMAIL_REMETENTE')
    senha_app = os.getenv('SENHA_APP')
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT'))

    # Buscar e-mail do destinatário no banco
    sessao = criar_sessao()
    usuario = sessao.query(Usuario).first()
    if not usuario:
        raise Exception("Nenhum usuário encontrado no banco.")

    email_destinatario = usuario.email

    # Caminho do relatório
    relatorio_path = Path(__file__).parent.parent / 'data' / 'relatorio_cidade.xlsx'

    # Criar mensagem de e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Relatório de Consumo de Energia por Cidade'
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg.set_content('Segue em anexo o relatório consolidado.')

    # Anexar arquivo
    with open(relatorio_path, 'rb') as f:
        file_data = f.read()
        file_name = relatorio_path.name

    msg.add_attachment(file_data, maintype='application',
                       subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                       filename=file_name)

    # Enviar e-mail
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp:
            smtp.login(email_remetente, senha_app)
            smtp.send_message(msg)
        print(f'✅ E-mail enviado com sucesso para {email_destinatario}!')
    except smtplib.SMTPAuthenticationError:
        print("❌ Falha de autenticação SMTP. Verifique o e-mail e a senha do app.")
    except smtplib.SMTPException as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
