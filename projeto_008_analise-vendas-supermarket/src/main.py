import pandas as pd
import matplotlib.pyplot as plt

# Caminho do dataset
FILEPATH = 'data/SuperMarket Analysis.csv'

# ------------------------- #
# 1. Leitura dos dados
# ------------------------- #
# Dataset de vendas de supermercado
# Cada linha representa uma transação
df = pd.read_csv(FILEPATH)

# ------------------------- #
# Análise 1
# Qual método de pagamento gera maior receita média por compra?
# ------------------------- #
payment_mean = (
    df.groupby("Payment")["Sales"]
      .mean()
      .sort_values(ascending=False)
)

print("\nReceita média por método de pagamento:")
print(payment_mean)

# ------------------------- #
# Análise 2
# Clientes Member gastam mais que clientes Normal?
# ------------------------- #
customer_mean = (
    df.groupby("Customer type")["Sales"]
      .mean()
      .sort_values(ascending=False)
)

print("\nGasto médio por tipo de cliente:")
print(customer_mean)

# ------------------------- #
# Análise 3
# Qual linha de produto gera maior lucro médio?
# ------------------------- #
product_profit = (
    df.groupby("Product line")["gross income"]
      .mean()
      .sort_values(ascending=False)
)

print("\nLucro médio por linha de produto:")
print(product_profit)
