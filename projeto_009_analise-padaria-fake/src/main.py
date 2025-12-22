import pandas as pd

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

    print("\nColunas:")
    print(df.columns.tolist())

    print("\nAmostra dos dados:")
    print(df.head())

if __name__ == "__main__":
    main()
