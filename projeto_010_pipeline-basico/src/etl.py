from pathlib import Path
import pandas as pd

# INPUT
input_path = Path("data/raw/vendas.csv")
if not input_path.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

df = pd.read_csv(input_path)

# TRANSFORM
df = df[df["valor"].notna() & (df["valor"] >= 0)]

df["data"] = pd.to_datetime(
    df["data"],
    format="%Y-%m-%d",
    errors="coerce"
)

df = df.dropna(subset=["data"])

if df.empty:
    raise ValueError("Dataset final está vazio após limpeza")
else:
    # OUTPUT
    output_path = Path("data/processed/vendas_limpa.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    if not output_path.exists():
        raise IOError(f"Falha ao salvar o arquivo: {output_path}")

print(f"Pipeline executado com sucesso: {len(df)} registros válidos")
