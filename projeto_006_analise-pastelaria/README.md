# Projeto 006 — Análise de Vendas da Pastelaria do Zé

## Problema
Pequenos comércios, como pastelarias, dificilmente possuem dados organizados para entender seu próprio desempenho.  
Sem registros consistentes, fica difícil saber quais produtos vendem mais, qual dia é mais lucrativo e quanto cada item gera de receita.

## Solução
Este script simula 30 dias de funcionamento de uma pastelaria, gera um dataset realista e realiza uma análise básica, incluindo:
- Tratamento de valores faltantes
- Detecção e correção de outliers
- Criação da métrica de receita
- Gráficos simples de receita diária e por item

O objetivo é demonstrar um fluxo completo e profissional de **data wrangling + análise**, usando Pandas e Matplotlib.

## Como usar
python main.py

## Exemplo de saída
    Resumo final:
             Data          Item  Quantidade  Preco  Receita
    0  2025-01-01  Pastel Carne           2      8       16
    1  2025-01-01        Queijo           5     10       50
    2  2025-01-01  Pastel Carne           1      7        7
    3  2025-01-01     Calabresa           3      6       18
    4  2025-01-01     Calabresa           4      9       36

    O script também gera dois gráficos:
    * Receita diária
    * Receita por item

## Melhorias futuras
- Adicionar margem de lucro por item
- Implementar sazonalidade (dias mais fracos/fortes)
- Exportar resultados para CSV