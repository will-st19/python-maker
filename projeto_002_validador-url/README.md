# Projeto 002 — Validador de URLs em Lote

## Problema
Empresas e profissionais lidam com listas de URLs em planilhas, relatórios, campanhas, landing pages e arquivos internos.  
Verificar manualmente se esses links estão ativos (200), redirecionando (301/302) ou quebrados (404/500) é trabalhoso e demorado.

## Solução
Este script recebe um arquivo CSV simples com uma coluna `url` e valida cada endereço:

- Código HTTP retornado  
- Status (válida / redireciona / quebrada / offline)  
- Tempo de resposta (ms)

O resultado é salvo em um novo CSV pronto para Excel, Data Studio ou BI.

## Como usar
python main.py urls.csv resultado.csv

## Exemplo de entrada
url
https://google.com
https://dominioquenaoexiste12345.com
https://httpstat.us/302


## Exemplo de saída
url,status_code,status,tempo_ms
https://google.com,200,valida,43
https://dominioquenaoexiste12345.com,0,offline,0
https://httpstat.us/302,302,redireciona,28

## Melhorias futuras
- Suporte a múltiplas threads para acelerar a validação
- Detecção do domínio raiz (whois, expiração, etc)
- Exportar relatório em JSON