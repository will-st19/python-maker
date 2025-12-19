import csv
import random
from datetime import datetime, timedelta
import os

CSV_PATH = "data/vendas_padaria.csv"
DELIMITER = ";"

PRODUTOS = [
    ("Pão Francês", "Padaria", 0.50),
    ("Café", "Bebidas", 2.50),
    ("Bolo", "Confeitaria", 4.00),
    ("Salgado", "Confeitaria", 5.00),
    ("Suco", "Bebidas", 3.50),
]

FORMAS_PAGAMENTO = ["Dinheiro", "Cartão", "Pix"]

def obter_menor_data_csv():
    """Retorna a menor data encontrada no CSV ou None se não houver dados."""
    if not os.path.exists(CSV_PATH):
        return None

    menor_data = None
    with open(CSV_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        next(reader, None)  # pula cabeçalho

        for row in reader:
            if not row:
                continue
            try:
                data = datetime.strptime(row[0], "%Y-%m-%d").date()
                if menor_data is None or data < menor_data:
                    menor_data = data
            except Exception:
                pass  # ignora linhas malformadas

    return menor_data


def criar_csv_se_nao_existir():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=DELIMITER)
            writer.writerow([
                "data",
                "hora",
                "produto",
                "categoria",
                "quantidade",
                "valor_unitario",
                "forma_pagamento"
            ])

def gerar_venda(data):
    produto, categoria, valor_unitario = random.choice(PRODUTOS)

    hora = f"{random.randint(6, 20):02d}:{random.randint(0, 59):02d}"
    quantidade = random.randint(1, 5)
    forma_pagamento = random.choice(FORMAS_PAGAMENTO)

    return [
        data.strftime("%Y-%m-%d"),
        hora,
        produto,
        categoria,
        quantidade,
        round(valor_unitario, 2),
        forma_pagamento
    ]

def gerar_dados(dias, vendas_por_dia=50):
    
    criar_csv_se_nao_existir()
    menor_data = obter_menor_data_csv()

    if menor_data:
        data_inicial = menor_data - timedelta(days=1)
    else:
        data_inicial = datetime.now().date()

    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=DELIMITER)

        for i in range(dias):
            data_atual = data_inicial - timedelta(days=i)

            for _ in range(vendas_por_dia):
                venda = gerar_venda(data_atual)
                writer.writerow(venda)


if __name__ == "__main__":
    gerar_dados(dias=7, vendas_por_dia=random.randint(30, 420))
    print("Dados gerados com sucesso.")
