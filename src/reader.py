import pandas as pd
from typing import Optional

def read_tickets(file_path: str) -> pd.DataFrame:
    """
    Lê o arquivo CSV de tickets e realiza as conversões iniciais de tipo.
    
    Args:
        file_path: Caminho para o arquivo CSV contendo os dados dos tickets.
        
    Returns:
        DataFrame do pandas com os dados formatados corretamente.
    """
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise RuntimeError(f"Erro ao ler o arquivo {file_path}: {e}")

    # Verificar colunas esperadas
    expected_columns = ['id', 'data_abertura', 'data_fechamento', 'analista', 'categoria', 'status', 'SLA_cumprido']
    for col in expected_columns:
        if col not in df.columns:
            raise ValueError(f"A coluna '{col}' é obrigatória e não foi encontrada no arquivo.")

    # Converter datas
    df['data_abertura'] = pd.to_datetime(df['data_abertura'])
    df['data_fechamento'] = pd.to_datetime(df['data_fechamento'], errors='coerce') # Para lidar com valores nulos

    # Garantir boolean para o SLA (pode vir como Sim/Não ou True/False)
    if df['SLA_cumprido'].dtype == object:
        df['SLA_cumprido'] = df['SLA_cumprido'].astype(str).str.lower().map({'sim': True, 'true': True, '1': True, 'não': False, 'nao': False, 'false': False, '0': False})
    else:
        df['SLA_cumprido'] = df['SLA_cumprido'].astype(bool)

    return df
