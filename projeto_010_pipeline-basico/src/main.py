import pandas as pd
import random
from pathlib import Path

data = [{
    "id": i,
    "valor": random.choice([round(random.uniform(10, 500), 2), None, -50]),
    "data": random.choice(["2024-01-10", "2024-13-40", None])
} for i in range(100)]

df = pd.DataFrame(data)

output_path = Path("data/raw/vendas.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)
