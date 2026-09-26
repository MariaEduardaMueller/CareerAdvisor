from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "vagas.csv"

def load_jobs(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {"id","cargo","empresa","area","nivel","localizacao","modalidade","salario","tecnologias"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes no dataset: {sorted(missing)}")
    df["salario"] = pd.to_numeric(df["salario"], errors="coerce")
    df["tecnologias"] = df["tecnologias"].fillna("")
    return df
