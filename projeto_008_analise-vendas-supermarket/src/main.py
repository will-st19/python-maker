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

top_payment = payment_mean.idxmax()
top_payment_value = payment_mean.max()

print(
    f"\n➡️ Método de pagamento com maior receita média: "
    f"{top_payment} (R$ {top_payment_value:.2f})"
)

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

top_customer = customer_mean.idxmax()
top_customer_value = customer_mean.max()

print(
    f"\n➡️ Tipo de cliente com maior gasto médio: "
    f"{top_customer} (R$ {top_customer_value:.2f})"
)

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

top_product = product_profit.idxmax()
top_product_value = product_profit.max()

print(
    f"\n➡️ Linha de produto com maior lucro médio: "
    f"{top_product} (R$ {top_product_value:.2f})"
)

# ------------------------- #
# Visualização simples
# ------------------------- #
# Receita média por método de pagamento
plt.figure(figsize=(6, 4))
payment_mean.plot(kind="bar")

plt.title("Receita Média por Método de Pagamento")
plt.xlabel("Método de Pagamento")
plt.ylabel("Receita Média (R$)")

# Ajuste de escala para destacar diferenças pequenas
y_min = payment_mean.min() * 0.98
y_max = payment_mean.max() * 1.02
plt.ylim(y_min, y_max)

plt.tight_layout()
plt.show()

print("\n--- Análise concluída com sucesso ---")
