<h1 align="center">📊 Incremental Sales Dataset Generator</h1>

<p align="center">
  Gerador simples e incremental de datasets de vendas fictícias em CSV.<br>
  Pensado para estudos em dados, pandas, SQL e visualização.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20evolução-blue" />
  <img src="https://img.shields.io/badge/python-3.x-green" />
  <img src="https://img.shields.io/badge/data-fake-lightgrey" />
</p>

---

## 🎯 Objetivo

Este projeto tem como objetivo **criar um dataset consistente e incremental** de vendas fictícias, simulando a operação diária de um pequeno comércio (ex: padaria).

A ideia não é gerar dados perfeitos, mas sim **dados plausíveis**, que permitam:
- prática com pandas
- análises exploratórias
- exercícios de SQL
- construção de dashboards
- simulação de perguntas reais de negócio

---

## 🧱 Estrutura inicial do dataset

O CSV gerado possui as seguintes colunas:

| Coluna           | Descrição            |
|------------------|----------------------|
| data             | Data da venda        |
| hora             | Horário da venda     |
| produto          | Nome do produto      |
| categoria        | Categoria do produto |
| quantidade       | Quantidade vendida   |
| valor_unitario   | Preço unitário       |
| forma_pagamento  | Meio de pagamento    |

Delimitador utilizado: `;`

---

## ⚙️ Como funciona

- O script cria o CSV caso ele não exista
- Novas execuções **não sobrescrevem dados**
- Cada execução adiciona vendas para dias anteriores
- O número de dias e vendas por dia é parametrizável

Isso permite que o dataset **cresça com o tempo**, simulando histórico.

---

## ▶️ Execução
python template_create_dataset.py