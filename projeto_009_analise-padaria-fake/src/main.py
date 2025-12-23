import pandas as pd
import plotly.express as px

CSV_PATH = "data/vendas_padaria.csv"

def main():
    colunas = [
        "data",
        "hora",
        "produto",
        "categoria",
        "quantidade",
        "valor_unitario",
        "forma_pagamento"
    ]

    df = pd.read_csv(
        CSV_PATH,
        sep=";",
        header=None,
        names=colunas
    )

    print("Dataset carregado com sucesso")
    print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")

    # ------------------------- #
    # Preparação
    # ------------------------- #
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["total_venda"] = df["quantidade"] * df["valor_unitario"]

    # ------------------------- #
    # Pergunta:
    # Qual foi o total de vendas por dia?
    # ------------------------- #
    vendas_por_dia = (
        df.groupby("data")["total_venda"]
          .sum()
          .reset_index()
          .sort_values("data")
    )

    print("\nTotal de vendas por dia:")
    print(vendas_por_dia)

    # ------------------------- #
    # Visualização simples
    # ------------------------- #
    fig = px.line(
        vendas_por_dia,
        x="data",
        y="total_venda",
        title="Faturamento Diário da Padaria",
        labels={
            "data": "Data",
            "total_venda": "Faturamento (R$)"
        }
    )

    fig.show()

if __name__ == "__main__":
    main()
