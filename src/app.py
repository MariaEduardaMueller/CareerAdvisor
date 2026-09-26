from .assistant import CareerAdvisor
from .llm import MODEL

def main():
    advisor = CareerAdvisor()
    print("CAREER ADVISOR — Assistente Inteligente de Carreira")
    print(f"Modelo local: {MODEL}")
    print(f"Base: {len(advisor.df)} vagas")
    print("Digite 'sair' para encerrar.\n")

    while True:
        question = input("Você: ").strip()
        if question.lower() in {"sair", "exit", "quit"}:
            print("\nAté mais!")
            break
        if not question:
            continue
        try:
            print(f"\nCareerAdvisor: {advisor.answer(question)}\n")
        except Exception as exc:
            print(f"\nErro ao consultar Ollama: {exc}")
            print("Verifique se o Ollama está executando e se OLLAMA_MODEL está correto.\n")

if __name__ == "__main__":
    main()
