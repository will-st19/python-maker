import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Simular Dataset de 30 dias
np.random.seed(47)

dias = pd.date_range(start="2025-01-01", periods=30, freq="D")
itens = ["Pastel Carne", "Pastel Frango", "Queijo", "Calabresa", "Coca-Cola", "Guaraná"]
prob_itens = [0.25, 0.20, 0.15, 0.15, 0.15, 0.10]

linhas = []

for dia in dias:
    vendas_dia = np.random.randint(8, 25)  # fluxo realista de vendas diárias

    for _ in range(vendas_dia):
        linhas.append({
            "Data": dia,
            "Item": np.random.choice(itens, p=prob_itens),
            "Quantidade": np.random.randint(1, 6),
            "Preco": np.random.choice([6, 7, 8, 9, 10])
        })

df = pd.DataFrame(linhas)

# Introduzir um valor faltante e um outlier
df.loc[5, "Quantidade"] = np.nan
df.loc[10, "Quantidade"] = 99  # Outlier absurdo

# Tratar valores faltantes
df.fillna({"Quantidade": df["Quantidade"].median()}, inplace=True)

# Detectar e tratar outliers pelo Z-score
z = np.abs(stats.zscore(df["Quantidade"]))
df.loc[z > 3, "Quantidade"] = df["Quantidade"].median()

# Criar coluna de Receita
df["Receita"] = df["Quantidade"] * df["Preco"]

# Insights simples → receita por dia
receita_dia = df.groupby("Data")["Receita"].sum()

plt.figure(figsize=(10,4))
plt.plot(receita_dia.index, receita_dia.values)
plt.title("Receita Diária – Pastelaria do Zé")
plt.xlabel("Data")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()

# 6. Item mais lucrativo
receita_item = df.groupby("Item")["Receita"].sum()
plt.figure(figsize=(8,4))
plt.bar(receita_item.index, receita_item.values)
plt.xticks(rotation=45)
plt.title("Receita por Item")
plt.xlabel("Item")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()

print("\nResumo final:")
print(df.head())