# Projeto 008 — Análise de Vendas de Supermercado

## Problema
Em operações de varejo, decisões simples como incentivar um meio de pagamento,
priorizar clientes fidelizados ou focar em determinadas categorias de produto
impactam diretamente a receita e o lucro.  
O problema aqui é responder perguntas básicas de negócio a partir de um CSV cru.

## Solução
O script carrega um dataset de vendas de supermercado e responde três perguntas
objetivas:
- Qual método de pagamento gera maior receita média por compra
- Se clientes Member gastam mais que clientes Normal
- Qual linha de produto apresenta maior lucro médio

A análise é feita com agregações simples, sem modelagem ou exageros.

## Como usar
python main.py

O arquivo CSV deve estar em:
data/SuperMarket Analysis.csv

## Exemplo de entrada
Invoice ID,Payment,Customer type,Product line,Sales,gross income
750-67-8428,Ewallet,Member,Health and beauty,548.97,26.14
226-31-3081,Cash,Normal,Electronic accessories,80.22,3.82

## Exemplo de saída
Receita média por método de pagamento:
Ewallet        335.50
Credit card    324.80
Cash           310.10

Gasto médio por tipo de cliente:
Member    330.20
Normal    305.40

Lucro médio por linha de produto:
Food and beverages    17.35
Health and beauty     16.90

## Melhorias futuras
- Adicionar visualizações simples (barplots)
- Analisar variação por cidade ou filial
- Comparar resultados ao longo do tempo (datas)