import pytest
import pandas as pd
from src.processor import get_executive_summary, get_analyst_ranking, get_category_distribution

@pytest.fixture
def sample_data():
    data = {
        'id': [1, 2, 3, 4],
        'analista': ['Joao', 'Maria', 'Joao', 'Pedro'],
        'categoria': ['Rede', 'Hardware', 'Rede', 'Acessos'],
        'status': ['Fechado', 'Fechado', 'Em aberto', 'Fechado'],
        'SLA_cumprido': [True, False, None, True]
    }
    return pd.DataFrame(data)

def test_executive_summary(sample_data):
    summary = get_executive_summary(sample_data)
    
    assert len(summary) == 4
    # Total
    assert summary[summary['Métrica'] == 'Total de Tickets']['Valor'].values[0] == 4
    # Fechados
    assert summary[summary['Métrica'] == 'Tickets Fechados']['Valor'].values[0] == 3
    # Abertos
    assert summary[summary['Métrica'] == 'Tickets Em Aberto']['Valor'].values[0] == 1
    # SLA (2 no prazo / 3 fechados) = 66.67%
    assert summary[summary['Métrica'] == 'Média SLA% (Fechados)']['Valor'].values[0] == '66.67%'

def test_analyst_ranking(sample_data):
    ranking = get_analyst_ranking(sample_data)
    
    assert len(ranking) == 3 # Joao, Maria, Pedro
    
    joao_stats = ranking[ranking['Analista'] == 'Joao']
    assert joao_stats['Tickets Fechados'].values[0] == 1 # Apenas o fechado conta
    assert joao_stats['Fechados no Prazo'].values[0] == 1
    assert joao_stats['SLA%'].values[0] == 100.0

def test_category_distribution(sample_data):
    dist = get_category_distribution(sample_data)
    
    assert len(dist) == 3
    assert dist[dist['Categoria'] == 'Rede']['Total de Tickets'].values[0] == 2
