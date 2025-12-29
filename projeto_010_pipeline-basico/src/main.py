import pandas as pd
import random
from pathlib import Path

def gerar_valor(valido, invalido):
    """
    Retorna:
    - 80% valor válido
    - 15% valor inválido
    - 5% None
    """
    r = random.random()

    if r < 0.80:
        return valido()
    elif r < 0.95:
        return invalido()
    else:
        return None


data = []

for i in range(120):
    registro = {
        "id": i,
        "valor": gerar_valor(
            lambda: round(random.uniform(10, 500), 2),
            lambda: -50
        ),
        "data": gerar_valor(
            lambda: "2024-01-10",
            lambda: "2024-13-40"
        ),
        "forma_pagamento": gerar_valor(
            lambda: random.choice(["credito", "debito", "pix"]),
            lambda: "bitcoin"
        )
    }

    data.append(registro)

df = pd.DataFrame(data)

output_path = Path("data/raw/vendas.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("Dataset gerado com dados válidos, inválidos e nulos.")
print(df.head())
