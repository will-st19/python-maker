# Projeto 01 — Extrator de Gastos Fixos a partir de Texto Solto

## Problema
As pessoas recebem valores de contas mensais em fontes diferentes:
e-mail, WhatsApp, PDF convertido, mensagens copiadas etc.  
Os valores ficam misturados no texto e o usuário não sabe quanto gasta no mês.

## Solução
Este script lê um arquivo `.txt` com qualquer texto colado nele
e extrai automaticamente todos os valores monetários no formato brasileiro
(ex.: R$ 19,90 — 29,00 — 150 — 2.345,67).  
O programa grava todos os valores identificados em um arquivo CSV limpo.

## Como usar
```
python main.py entrada.txt saida.csv
```

## Exemplo de entrada
```
Netflix renovada: R$ 55,90
Internet: 99,90
Academia (mensalidade): 129
Cartão: 2.345,77 vencimento 10/10
Promoção aleatória: 9,99
```

## Exemplo de saída
```
valor
55.90
99.90
129.00
2345.77
9.99
```

## Melhorias futuras
- Somar automaticamente o total mensal
- Identificar categorias por palavra-chave (ex.: "internet")
- Criar gráficos simples com histórico
- Transformar em interface Tkinter ou API Flask

## Refinamento da Extração: 
Investigar o falso positivo causado por números 
com ponto que não são monetários (ex: temperaturas, datas) 
para garantir que apenas valores com vírgula decimal 
ou prefixo "R$" sejam incluídos, aprimorando a precisão do RegEx.