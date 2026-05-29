import pandas as pd
from typing import Tuple

def filter_period(df: pd.DataFrame, days: int = 7) -> pd.DataFrame:
    """
    Filtra os tickets baseado em um período de tempo. 
    (Para simplificação, pegaremos apenas os mais recentes).
    Na vida real isso seria com base na data_abertura ou data_fechamento relativa ao now().
    """
    # Simplificação: Não filtramos por data agora para usar todos os dados do mock, 
    # mas a lógica estaria aqui.
    return df.copy()

def get_executive_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Gera os dados para a aba de Resumo Executivo."""
    total_tickets = len(df)
    total_fechados = len(df[df['status'].str.lower() == 'fechado'])
    total_abertos = total_tickets - total_fechados
    
    if total_fechados > 0:
        tickets_no_prazo = len(df[(df['status'].str.lower() == 'fechado') & (df['SLA_cumprido'] == True)])
        media_sla = round((tickets_no_prazo / total_fechados) * 100, 2)
    else:
        media_sla = 0.0

    summary_data = {
        'Métrica': ['Total de Tickets', 'Tickets Fechados', 'Tickets Em Aberto', 'Média SLA% (Fechados)'],
        'Valor': [total_tickets, total_fechados, total_abertos, f"{media_sla}%"]
    }
    return pd.DataFrame(summary_data)

def get_analyst_ranking(df: pd.DataFrame) -> pd.DataFrame:
    """Gera os dados para a aba de Ranking de Analistas."""
    df_fechados = df[df['status'].str.lower() == 'fechado'].copy()
    
    if df_fechados.empty:
        return pd.DataFrame(columns=['Analista', 'Tickets Fechados', 'Fechados no Prazo', 'SLA%'])

    # Agrupar por analista
    ranking = df_fechados.groupby('analista').agg(
        total_fechados=('id', 'count'),
        fechados_no_prazo=('SLA_cumprido', 'sum')
    ).reset_index()

    ranking['SLA%'] = round((ranking['fechados_no_prazo'] / ranking['total_fechados']) * 100, 2)
    
    # Ordenar
    ranking = ranking.sort_values(by=['total_fechados', 'SLA%'], ascending=[False, False])
    
    # Renomear colunas
    ranking = ranking.rename(columns={
        'analista': 'Analista',
        'total_fechados': 'Tickets Fechados',
        'fechados_no_prazo': 'Fechados no Prazo'
    })
    
    return ranking

def get_category_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """Gera os dados para a aba de Distribuição por Categoria."""
    distribution = df.groupby('categoria').agg(total=('id', 'count')).reset_index()
    distribution = distribution.sort_values(by='total', ascending=False)
    distribution = distribution.rename(columns={'categoria': 'Categoria', 'total': 'Total de Tickets'})
    return distribution

def process_data(df: pd.DataFrame, days: int = 7) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Orquestra as funções de processamento e retorna os 3 DataFrames."""
    df_period = filter_period(df, days)
    
    df_summary = get_executive_summary(df_period)
    df_ranking = get_analyst_ranking(df_period)
    df_categories = get_category_distribution(df_period)
    
    return df_summary, df_ranking, df_categories
