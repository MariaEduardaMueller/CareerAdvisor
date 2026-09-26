# 03 — Prompts

O system prompt está em `src/prompts.py`.

### Regras
- Responder em português.
- Usar somente o contexto fornecido.
- Não inventar vagas, empresas, salários ou tecnologias.
- Diferenciar dados da base de afirmações sobre o mercado.
- Informar quando a base for insuficiente.

### Edge case
Pergunta: `Qual empresa tem a melhor cultura organizacional?`

Comportamento esperado: informar que a base não possui dados de cultura organizacional.

Pergunta: `Qual é a melhor carreira em tecnologia?`

Comportamento esperado: não escolher uma "melhor" carreira; explicar o que pode ser observado na base.
