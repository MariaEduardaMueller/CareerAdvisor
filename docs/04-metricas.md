# 04 — Avaliação e Métricas

## Métricas
**Aderência aos dados:** números e fatos devem ser verificáveis no contexto.

**Taxa de resposta segura:** percentual de casos em que o agente reconhece corretamente que faltam dados.

**Relevância:** a resposta trata diretamente da pergunta.

**Não alucinação:** não apresenta fatos ausentes como se fossem verdade.

**Transparência:** diferencia a amostra do mercado real.

## Execução
```bash
pytest -q
python -m tests.run_evaluation
```

`tests/evaluation_dataset.json` contém os cenários. A camada determinística é validada por testes Python; a resposta final do Llama pode ser avaliada manualmente ou futuramente com DeepEval/LLM-as-a-Judge.
