import os
import sys
import logging
from reader import read_tickets
from processor import process_data
from exporter import export_to_excel
from simulator import generate_mock_tickets
from mailer import send_email_with_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PipelineGovernanca")

def load_env_vars():
    return {
        'INPUT_FILE_PATH': os.getenv('INPUT_FILE_PATH', 'data/tickets.csv'),
        'OUTPUT_DIR': os.getenv('OUTPUT_DIR', 'output/'),
        'PERIODO_DIAS': int(os.getenv('PERIODO_DIAS', 30)),
        'RUN_SIMULATOR': os.getenv('RUN_SIMULATOR', 'true').lower() == 'true',
        'SIMULATOR_COUNT': int(os.getenv('SIMULATOR_TICKETS_COUNT', 1000)),
        'SMTP_SERVER': os.getenv('SMTP_SERVER', ''),
        'SMTP_PORT': int(os.getenv('SMTP_PORT', 587)),
        'EMAIL_SENDER': os.getenv('EMAIL_SENDER', ''),
        'EMAIL_PASSWORD': os.getenv('EMAIL_PASSWORD', ''),
        'EMAIL_RECIPIENT': os.getenv('EMAIL_RECIPIENT', '')
    }

def main():
    try:
        env = load_env_vars()
        input_file = env['INPUT_FILE_PATH']
        output_dir = env['OUTPUT_DIR']
        
        # 0. Simulação (Opcional)
        if env['RUN_SIMULATOR']:
            logger.info(f"Modo Simulador ativado. Gerando {env['SIMULATOR_COUNT']} tickets falsos...")
            generate_mock_tickets(input_file, env['SIMULATOR_COUNT'])
            logger.info("Simulação concluída com sucesso.")

        # 1. Leitura
        logger.info(f"Lendo dados de {input_file}...")
        df_tickets = read_tickets(input_file)
        logger.info(f"Dados carregados. Total: {len(df_tickets)} registros.")

        # 2. Processamento
        logger.info("Processando métricas e rankings...")
        df_summary, df_ranking, df_categories = process_data(df_tickets, days=env['PERIODO_DIAS'])

        # 3. Exportação
        logger.info("Gerando arquivo Excel...")
        output_path = export_to_excel(df_summary, df_ranking, df_categories, output_dir)
        logger.info(f"Relatório salvo em: {output_path}")

        # 4. Envio de E-mail
        if env['SMTP_SERVER'] and env['EMAIL_PASSWORD'] and env['EMAIL_PASSWORD'] != 'sua_senha_de_aplicativo_aqui':
            logger.info("Enviando relatório por e-mail...")
            send_email_with_report(
                output_path, 
                env['SMTP_SERVER'], 
                env['SMTP_PORT'], 
                env['EMAIL_SENDER'], 
                env['EMAIL_PASSWORD'], 
                env['EMAIL_RECIPIENT']
            )
            logger.info("E-mail enviado com sucesso!")
        else:
            logger.warning("Credenciais de e-mail não configuradas. Pulando o envio.")

        sys.exit(0)

    except Exception as e:
        logger.error(f"Erro no pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
