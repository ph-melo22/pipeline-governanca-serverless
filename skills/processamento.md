# Skill: Processamento e Regras de Negócio

Este arquivo define como calcular os rankings e as métricas do relatório.

## 1. Ranking de Analistas
- **Filtro:** Apenas tickets com status "Fechado" devem ser considerados no ranking.
- **Métricas por analista:**
  - `total_fechados`: Contagem de tickets fechados pelo analista no período.
  - `fechados_no_prazo`: Contagem de tickets onde `SLA_cumprido` é True.
  - `SLA_percentual`: `(fechados_no_prazo / total_fechados) * 100` (arredondado para 2 casas decimais).
- **Ordenação:** Ordenar de forma decrescente primeiro por `total_fechados`, depois por `SLA_percentual`.

## 2. Tickets por Categoria
- Agrupamento simples de todos os tickets (abertos e fechados) por `categoria`.
- Contagem total por categoria para entender o volume de demandas de cada área.

## 3. Resumo Executivo
- Contagem do total geral de tickets no arquivo.
- Total de tickets "Fechados" versus "Em aberto".
- Média geral de SLA% (total de tickets fechados no prazo / total de tickets fechados).
