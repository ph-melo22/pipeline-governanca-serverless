# Skill: Exportação (Geração de Excel)

Este arquivo orienta como formatar a saída final usando `openpyxl`.

## Requisitos do Arquivo
- **Nome:** `relatorio_YYYY-MM-DD.xlsx` (onde YYYY-MM-DD é a data de geração).
- **Destino:** Pasta definida pela variável de ambiente `OUTPUT_DIR`.

## Abas Necessárias (Planilhas)
O arquivo final deve ter exatamente 3 abas, nesta ordem:
1. **Resumo Executivo**: Contém as métricas gerais do período.
2. **Ranking Analistas**: Lista ordenada dos analistas, quantidade de tickets e % de SLA.
3. **Por Categoria**: Volume de tickets divididos por categoria.

## Estilização Básica (Opcional, mas desejada)
- Linha de cabeçalho em negrito.
- Ajuste automático (ou aproximado) da largura das colunas.
- Formatação da coluna de SLA% como porcentagem no Excel (se possível).
