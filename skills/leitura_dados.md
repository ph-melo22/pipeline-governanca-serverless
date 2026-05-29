# Skill: Leitura de Dados

Este arquivo define as expectativas para a leitura de dados de entrada do sistema de ticketing.

## Formato de Entrada
O sistema lê primariamente arquivos CSV contendo o dump dos tickets.

## Colunas Esperadas
O DataFrame do Pandas resultante da leitura deve conter as seguintes colunas (no mínimo):
- `id`: (string/int) Identificador único do ticket.
- `data_abertura`: (datetime) Data e hora de abertura.
- `data_fechamento`: (datetime ou nulo) Data e hora de fechamento do ticket.
- `analista`: (string) Nome do analista responsável.
- `categoria`: (string) Categoria do incidente/requisição (ex: Rede, Hardware, Acessos).
- `status`: (string) Status do ticket (ex: Fechado, Em aberto, Pendente).
- `SLA_cumprido`: (boolean/string 'Sim' ou 'Não') Indicador se o SLA foi cumprido.

## Tratamentos Essenciais na Leitura
- Converter `data_abertura` e `data_fechamento` para objetos datetime.
- Tratar campos nulos em `data_fechamento` para tickets em aberto.
- Garantir que `SLA_cumprido` seja um valor booleano ou numérico tratável para cálculo de porcentagem.
