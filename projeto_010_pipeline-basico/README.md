# Projeto 010 — Pipeline Básico

## Problema
Dados de vendas vindos de sistemas simples ou legados frequentemente chegam incompletos, inconsistentes ou inválidos.
Valores podem estar negativos ou ausentes, datas podem ter formatos incorretos e não existe garantia de qualidade mínima para análise ou carregamento em banco de dados.

Esse cenário impede:

- análises confiáveis
- uso direto em SQL
- reaproveitamento do dataset por outras áreas

Sem um tratamento básico, qualquer relatório ou decisão baseada nesses dados se torna frágil.

## Solução
O projeto implementa um pipeline ETL simples e funcional, dividido em duas etapas claras:

1. Geração de dados brutos (main.py)

- Cria um dataset propositalmente sujo
- Introduz valores nulos, negativos e datas inválidas
- Simula dados próximos da realidade operacional

2. Limpeza e transformação (etl.py)

- Remove registros com valores inválidos
- Normaliza e valida datas com formato explícito
- Garante um dataset final consistente e pronto para uso

O resultado é um arquivo limpo, com regras claras de qualidade, adequado para análises ou carga em banco (ex: SQLite).

## Como usar
python main.py   # gera o dataset bruto (data/raw)
python etl.py    # limpa e gera o dataset tratado (data/processed)

## Melhorias futuras
- Persistir os dados tratados em um banco SQLite
- Criar testes automáticos para validação de schema e qualidade
- Gerar relatório simples de dados descartados (data quality)
- Parametrizar regras de limpeza (ex: limites de valor, formatos de data)
- Versionar datasets por data de execução
- Adaptar o pipeline para leitura de fontes externas (API ou CSV real)