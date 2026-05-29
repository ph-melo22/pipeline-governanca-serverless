import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_mock_tickets(output_path: str, num_tickets: int = 1000):
    """
    Gera um CSV com tickets fictícios, simulando o comportamento de um ITSM.
    """
    analistas = ['João Silva', 'Maria Souza', 'Pedro Henrique', 'Ana Clara', 'Carlos Eduardo', 'Luiza Campos']
    categorias = ['Rede', 'Hardware', 'Acessos', 'Software', 'Dúvidas Gerais']
    status_options = ['Fechado', 'Fechado', 'Fechado', 'Em aberto'] # Maior probabilidade de estar fechado
    
    data = []
    now = datetime.now()
    
    for i in range(1, num_tickets + 1):
        # Abertura entre 1 a 30 dias atrás
        dias_atras = random.randint(1, 30)
        horas_atras = random.randint(0, 23)
        minutos_atras = random.randint(0, 59)
        data_abertura = now - timedelta(days=dias_atras, hours=horas_atras, minutes=minutos_atras)
        
        status = random.choice(status_options)
        
        if status == 'Fechado':
            # Tempo de resolução (SLA) variando de 1 hora a 10 dias
            horas_resolucao = random.randint(1, 240)
            data_fechamento = data_abertura + timedelta(hours=horas_resolucao)
            
            # Se o fechamento for maior que agora, limitamos ao momento atual
            if data_fechamento > now:
                data_fechamento = now
                
            # Simulando o SLA (80% das vezes é cumprido)
            sla_cumprido = random.choices([True, False], weights=[80, 20])[0]
        else:
            data_fechamento = None
            sla_cumprido = None
            
        data.append({
            'id': i,
            'data_abertura': data_abertura.strftime('%Y-%m-%d %H:%M:%S'),
            'data_fechamento': data_fechamento.strftime('%Y-%m-%d %H:%M:%S') if data_fechamento else '',
            'analista': random.choice(analistas),
            'categoria': random.choice(categorias),
            'status': status,
            'SLA_cumprido': 'Sim' if sla_cumprido is True else ('Não' if sla_cumprido is False else '')
        })
        
    df = pd.DataFrame(data)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    return output_path
