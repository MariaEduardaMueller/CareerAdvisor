# 🤖 CareerAdvisor — Assistente Virtual de Carreira com IA Generativa

Projeto para o desafio **Construa seu Assistente Virtual com Inteligência Artificial**, da DIO. O CareerAdvisor combina **Python + Pandas + CSV + Llama local via Ollama** para responder perguntas sobre uma base de vagas de tecnologia.

> **Importante:** os registros de `data/vagas.csv` são fictícios e servem apenas para demonstração.

## Objetivo

Responder perguntas sobre cargos, áreas, níveis, tecnologias, modalidades e salários disponíveis na base, deixando explícito quando os dados são insuficientes.

## Arquitetura

```text
Usuário
   ↓
Python / CareerAdvisor
   ├── Pandas → vagas.csv
   ↓
Contexto estruturado
   ↓
Prompt com regras anti-alucinação
   ↓
Llama local / Ollama
   ↓
Resposta
```

## Estrutura

```text
career-advisor/
├── data/
│   ├── vagas.csv
│   └── README.md
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── evidencias/
│   ├── evi_dadosforadabase.png
│   ├── evi_evaluation1.png
│   ├── evi_exec1.png
│   ├── evi_exec2.png
│   ├── evi_exec3.png
│   ├── evi_exec4.png
│   └── evi_pytest.png
├── logs/
│   ├── logs.txt
│   └── logs_evaluations.txt
├── results/
│   └── README.md
├── src/
│   ├── app.py
│   ├── assistant.py
│   ├── data_loader.py
│   ├── data_query.py
│   ├── llm.py
│   └── prompts.py
└── tests/
    ├── evaluation_dataset.json
    ├── run_evaluation.py
    └── test_data_query.py
├── README.md
└── requirements.txt
```

## Tecnologias

Python, Pandas, Requests, Ollama, Llama, Pytest, CSV e engenharia de prompts.

## Como executar

### 1. Criar ambiente

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 2. Instalar

```bash
pip install -r requirements.txt
```

### 3. Verificar seu Llama

```bash
ollama list
```

O projeto usa por padrão:

```text
llama3.2
```

Se o seu modelo tiver outro nome:

**PowerShell**
```powershell
$env:OLLAMA_MODEL="SEU_MODELO"
```

**Linux/macOS**
```bash
export OLLAMA_MODEL="SEU_MODELO"
```

### 4. Iniciar o Ollama

```bash
ollama serve
```

### 5. Rodar

Na raiz do projeto:

```bash
python -m src.app
```

Exemplo:

```text

CAREER ADVISOR — Assistente Inteligente de Carreira
Modelo local: llama3.2
Base: 20 vagas
Digite 'sair' para encerrar.

Você: Quantas vagas exigem Python?

CareerAdvisor:
...
```

## Testes

```bash
pytest -q
```

## Avaliação

```bash
python -m tests.run_evaluation
```

Os casos ficam em `tests/evaluation_dataset.json`.

As dimensões são:
- aderência aos dados;
- relevância;
- não alucinação;
- resposta segura;
- transparência sobre limitações.

## Estratégia anti-alucinação

A aplicação **consulta o CSV antes de chamar o Llama**. O modelo recebe apenas um contexto derivado dos dados e instruções para não inventar informações.

Exemplo de pergunta fora da base:

> Qual empresa tem a melhor cultura organizacional?

Comportamento esperado:

> A base não possui informações suficientes sobre cultura organizacional.

Isso evita apresentar uma opinião ou conhecimento externo como se viesse do dataset.

## Etapas do desafio

| Etapa | Implementação |
|---|---|
| 1. Documentação | `docs/01-documentacao-agente.md` |
| 2. Base de conhecimento | `data/vagas.csv` + `docs/02-base-conhecimento.md` |
| 3. Prompts | `src/prompts.py` + `docs/03-prompts.md` |
| 4. Aplicação funcional | `src/` |
| 5. Avaliação e métricas | `tests/` + `docs/04-metricas.md` |
| 6. Pitch | `docs/05-pitch.md` |

## Evoluções possíveis

- Interface Streamlit;
- dataset público real;
- RAG/embeddings;
- DeepEval;
- LLM-as-a-Judge;
- gráficos;
- upload de CSV;
- comparação entre modelos locais.

## Autora

**Maria Eduarda Mueller**

Projeto desenvolvido como parte dos desafios da trilha **Bradesco Dados, Cibersegurança & GenAI — DIO**.
