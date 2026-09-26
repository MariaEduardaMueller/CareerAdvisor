import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import load_jobs
from src.data_query import query_context


def main():
    root = Path(__file__).resolve().parents[1]
    cases = json.loads((root / "tests/evaluation_dataset.json").read_text(encoding="utf-8"))
    df = load_jobs()

    print("AVALIAÇÃO DETERMINÍSTICA — CAREER ADVISOR")
    print(f"Base avaliada: {len(df)} vagas")
    print("Filtros, contagens, médias e ordenações são executados por Python/Pandas.")

    for case in cases:
        print(f"\nCaso {case['id']}: {case['question']}")
        print(f"Esperado: {case['expected_behavior']}")
        print("-" * 80)
        print(query_context(df, case["question"]))


if __name__ == "__main__":
    main()
