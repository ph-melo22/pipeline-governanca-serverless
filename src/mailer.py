import smtplib
from email.message import EmailMessage
import os

def send_email_with_report(report_path: str, smtp_server: str, smtp_port: int, sender: str, password: str, recipient: str):
    """Envia um e-mail com o arquivo do relatório em anexo."""
    
    if not all([smtp_server, sender, password, recipient]):
        raise ValueError("Configurações de e-mail ausentes no .env. Pulei o envio de e-mail.")
        
    msg = EmailMessage()
    msg['Subject'] = 'Relatório Semanal de Governança de TI'
    msg['From'] = sender
    msg['To'] = recipient
    
    body = f"""
Olá!

Segue em anexo o relatório semanal automatizado de tickets de ITSM, com os Rankings de Analistas e métricas de SLA.
Este arquivo foi processado com uma massa de dados de teste (Simulador).

Este é um relatório gerado de forma totalmente autônoma pelo nosso Pipeline Agentic.

Atenciosamente,
Seu Agentic Pipeline
    """
    msg.set_content(body)
    
    # Anexar o arquivo Excel
    try:
        with open(report_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(report_path)
            
        msg.add_attachment(
            file_data, 
            maintype='application', 
            subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', 
            filename=file_name
        )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo de relatório {report_path} não encontrado para envio.")
        
    # Conexão SMTP e envio
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() # Protege a conexão
        server.login(sender, password)
        server.send_message(msg)
