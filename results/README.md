# Resultados — CareerAdvisor

Esta pasta reúne os resultados e evidências gerados durante a avaliação do **CareerAdvisor — Assistente Inteligente de Carreira**.

Os resultados registrados aqui servem como evidência das execuções realizadas durante o desenvolvimento e validação do projeto.

---

## 1. Avaliação determinística

A avaliação determinística verifica se filtros, contagens, médias salariais, ordenações e regras de disponibilidade são executados corretamente pela aplicação.

A execução é realizada com:

```bash
python -m tests.run_evaluation
```

A avaliação utiliza **Python/Pandas** para processar a base de vagas antes que o LLM seja utilizado para formular a resposta.

### Resultado da execução

A avaliação final contém **14 casos de teste**, identificados de `CA-01` a `CA-14`.

Os casos abrangem:

* frequência de tecnologias;
* quantidade de vagas por tecnologia;
* média salarial;
* distribuição por modalidade;
* filtros combinados de área e modalidade;
* filtros combinados de tecnologia e modalidade;
* maiores salários;
* comparação entre níveis;
* consultas com múltiplos critérios;
* tratamento de informações inexistentes na base.

### Principais resultados

| Caso  | Verificação                                  | Resultado                          |
| ----- | -------------------------------------------- | ---------------------------------- |
| CA-01 | Tecnologias nas vagas de Dados               | Frequências calculadas pelo Python |
| CA-02 | Vagas que exigem Python                      | 18 vagas                           |
| CA-03 | Média salarial das vagas com AWS             | R$ 6.133,33                        |
| CA-04 | Modalidade mais frequente                    | Remoto: 10 vagas                   |
| CA-05 | Vagas remotas de Engenharia de Dados         | 3 vagas                            |
| CA-06 | Vagas remotas com Power BI                   | 1 vaga                             |
| CA-07 | Maiores salários                             | Top 5 calculado pelo Python        |
| CA-08 | Cultura organizacional                       | Informação indisponível            |
| CA-09 | Plano de carreira                            | Informação indisponível            |
| CA-10 | Benefícios                                   | Informação indisponível            |
| CA-11 | Taxa de promoção                             | Informação indisponível            |
| CA-12 | Comparação entre estágio e júnior em Dados   | 4 vagas                            |
| CA-13 | Vagas remotas que utilizam AWS               | 3 vagas                            |
| CA-14 | Média salarial de Engenharia de Dados remota | R$ 5.733,33                        |

A base utilizada na avaliação contém **20 vagas fictícias**.

---

## 2. Testes automatizados

Além da avaliação dos casos de uso, o projeto possui testes automatizados para verificar o comportamento das funções responsáveis pela consulta e filtragem dos dados.

Execução:

```bash
pytest -q
```

Resultado final:

```text
8 passed
```

Isso confirma que os testes automatizados definidos para o projeto foram executados com sucesso.

---

## 3. Princípio de avaliação

O CareerAdvisor utiliza uma separação entre:

```text
Pergunta do usuário
        ↓
Python / Pandas
        ↓
Filtro e cálculo determinístico
        ↓
Contexto estruturado
        ↓
Prompt com regras de segurança
        ↓
LLM local
        ↓
Resposta em linguagem natural
```

Dessa forma, informações quantitativas e filtros importantes não dependem exclusivamente da interpretação do modelo.

Por exemplo:

* quantidade de vagas;
* médias salariais;
* maiores salários;
* combinação de filtros;
* modalidades;
* tecnologias presentes na base.

Esses valores são calculados diretamente a partir do CSV.

O LLM recebe o contexto estruturado e é responsável principalmente pela **formulação da resposta em linguagem natural**.

---

## 4. Tratamento de informações indisponíveis

A avaliação também verifica o comportamento do assistente quando o usuário solicita informações que não existem na base.

Exemplos:

* cultura organizacional;
* plano de carreira;
* benefícios;
* taxa de promoção.

Nesses casos, o sistema deve informar que o dado não está disponível e evitar inferências baseadas em informações não relacionadas.

O objetivo é reduzir respostas inventadas e manter a resposta limitada ao conhecimento disponível na base.

---

## 5. Base de dados

A avaliação utiliza uma base **fictícia**, criada exclusivamente para demonstração do projeto.

Portanto, os resultados não representam:

* o mercado de trabalho real;
* médias salariais reais;
* ranking real de empresas;
* condições reais de contratação;
* benefícios reais;
* cultura organizacional das empresas.

Os valores apresentados devem ser interpretados somente como resultados da base de demonstração utilizada pelo CareerAdvisor.

---

## 6. Evidências

As evidências foram documentadas por meio de prints e arquivos .txt. A estrutura dos arquivos de evidência podem ser encontrados em:
```text
results/
├── README.md
├── evidencias/
│   ├── evi_dadosforadabase.png
│   ├── evi_evaluation1.png
│   ├── evi_exec1.png
│   ├── evi_exec2.png
│   ├── evi_exec3.png
│   ├── evi_exec4.png
│   ├── evi_exec1.png
│   └── evi_pytest.png
└── logs/
    ├── logs.txt
    └── logs_evaluations.txt
```
---

## 7. Observação

Os resultados desta pasta representam a execução da versão final do projeto e devem ser analisados em conjunto com a documentação presente em `docs/`.

A avaliação tem como objetivo demonstrar principalmente **rastreabilidade, determinismo nas consultas estruturadas e controle contra alucinação**, mantendo o LLM dentro dos limites definidos para o CareerAdvisor.
