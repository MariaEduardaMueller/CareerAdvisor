# 02 — Base de Conhecimento

A base é `data/vagas.csv`, um dataset fictício para demonstração.

### Campos
- `id`: identificador
- `cargo`: cargo
- `empresa`: empresa fictícia
- `area`: área
- `nivel`: nível
- `localizacao`: localização
- `modalidade`: remoto, híbrido ou presencial
- `salario`: valor do dataset
- `tecnologias`: tecnologias separadas por `;`

### Operações
A camada Pandas filtra vagas, calcula salário médio, frequência de tecnologias, quantidade de vagas e distribuição por modalidade.

### Grounding
O Llama não recebe o CSV como conhecimento implícito: a aplicação primeiro consulta os dados e só então passa o contexto relevante ao modelo.
