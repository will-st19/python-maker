# Projeto 009 — Análise de Vendas (Padaria Fake)

## Visão geral
Este projeto simula vendas de uma padaria/pastelaria fictícia e realiza
uma análise inicial do dataset usando **Pandas**.

A ideia não é complexidade, mas **base sólida**:
ler dados corretamente, entender a estrutura e preparar o terreno
para análises de negócio mais inteligentes no futuro.

## Objetivo atual
- Carregar um CSV de vendas
- Definir explicitamente o schema do dataset
- Validar volume, colunas e amostra dos dados

Este é o **ponto zero da análise**.

## Estrutura do dataset
O arquivo CSV segue o padrão:

data;hora;produto;categoria;quantidade;valor_unitario;forma_pagamento
2025-12-19;09:09;Bolo;Confeitaria;1;4.0;Pix
2025-12-19;18:35;Salgado;Confeitaria;4;5.0;Dinheiro

## Como usar
python main.py

O arquivo CSV deve estar em:
data/vendas_padaria.csv

## Saída esperada
- Confirmação de carregamento do dataset
- Número de linhas e colunas
- Lista de colunas
- Amostra das primeiras linhas

## Próximos passos (planejados)
- Validação de tipos de dados
- Cálculo de faturamento
- Produto mais vendido
- Análises por categoria e forma de pagamento
- Evolução do dataset (novos produtos, regras mais realistas)