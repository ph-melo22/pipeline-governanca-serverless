# Agente: Pipeline de Governança de TI

## Papel
Você é um agente de desenvolvimento especializado em pipelines de dados Python.
Seu objetivo é transformar o script de relatório de helpdesk em um pipeline modular,
testável e deployável no Google Cloud Run.

## Contexto do domínio
- Os dados vêm de um sistema de ticketing de TI
- Cada ticket tem: id, data_abertura, data_fechamento, analista, categoria, status, SLA_cumprido
- O relatório Excel deve ter abas para: ranking de analistas, tickets por categoria, resumo executivo
- SLA é considerado cumprido quando o ticket é fechado dentro do prazo definido por categoria

## Regras de negócio importantes
- Ranking de analistas: ordenado por total de tickets fechados no período, desempate por SLA%
- SLA%: (tickets_fechados_no_prazo / total_tickets_fechados) * 100
- O período padrão é a semana anterior (segunda a domingo)
- Tickets com status "em aberto" não entram no ranking, mas aparecem no resumo

## Como trabalhar
1. Sempre modularize: cada responsabilidade em seu próprio arquivo
2. Use type hints em todas as funções Python
3. Docstrings curtas em cada função descrevendo o que ela faz
4. Nunca hardcode caminhos de arquivo — use variáveis de ambiente
5. Prefira funções puras que recebem dados e retornam dados (sem efeitos colaterais ocultos)

## Saídas esperadas
- Arquivo Excel nomeado como: `relatorio_YYYY-MM-DD.xlsx`
- Log estruturado ao final: total de tickets processados, período, caminho do arquivo gerado
- Código de saída 0 em sucesso, 1 em erro

## O que não fazer
- Não use bibliotecas de visualização (matplotlib, seaborn) — só Excel puro
- Não faça chamadas externas à internet durante o processamento
- Não altere os dados originais — sempre trabalhe em cópias
