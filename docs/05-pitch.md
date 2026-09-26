# 05 — Pitch
# Pitch — CareerAdvisor

### Duração aproximada: 3 minutos

## 1. Abertura — 20 segundos

Olá, eu sou Maria Eduarda Mueller e o projeto que eu desenvolvi é o **CareerAdvisor, um assistente inteligente de carreira voltado para vagas na área de tecnologia**.

A ideia surgiu de uma situação muito comum para quem está começando ou buscando uma oportunidade na área de tecnologia: existem muitas vagas, muitas tecnologias diferentes e muitas informações para analisar, mas nem sempre é fácil transformar esses dados em uma informação rápida e objetiva.

---

## 2. A dor do usuário — 30 segundos

A principal dor que eu quis trabalhar foi justamente a **dificuldade de consultar e interpretar informações de várias vagas de tecnologia**.

Por exemplo, uma pessoa pode querer saber:

* quantas vagas exigem Python;
* quais vagas são remotas;
* qual é a média salarial de determinadas vagas;
* quais tecnologias aparecem com mais frequência;
* ou comparar oportunidades de diferentes níveis.

O problema é que um assistente baseado apenas em um modelo de linguagem poderia simplesmente gerar uma resposta plausível, mas incorreta.

E, quando estamos falando de salário, requisitos ou características de vagas, **inventar uma informação é um problema sério**.

---

## 3. Por que escolhi esse projeto — 20 segundos

Eu escolhi esse tema porque ele também está diretamente relacionado à minha área de interesse, que é **Dados**.

Além disso, eu queria explorar uma aplicação de IA que não dependesse apenas da geração de texto, mas que utilizasse **dados estruturados, processamento com Python e uma camada de inteligência artificial**.

Por isso, o CareerAdvisor foi pensado como uma combinação entre **Data Analysis e IA generativa**.

---

## 4. A solução — 40 segundos

A solução é um assistente que consulta uma base estruturada de vagas e responde às perguntas do usuário em linguagem natural.

A arquitetura funciona basicamente assim:

**Usuário → Python/Pandas → filtro e cálculo → contexto estruturado → LLM → resposta.**

O ponto importante é que o LLM **não é responsável por calcular os dados principais**.

Se o usuário pergunta, por exemplo, quantas vagas exigem Python, o Python consulta o CSV e calcula a quantidade.

Se pergunta a média salarial das vagas que exigem AWS, o sistema primeiro filtra as vagas com AWS e depois calcula a média.

Só depois disso o resultado é enviado para o modelo de linguagem, que transforma aquela informação em uma resposta mais natural.

---

## 5. O diferencial — 35 segundos

E esse é o principal diferencial do projeto.

Eu não quis criar apenas um chatbot que responde perguntas sobre vagas.

Eu quis criar um assistente com uma preocupação explícita com **confiabilidade e controle de alucinações**.

Por isso, existem regras para o modelo:

* não inventar empresas;
* não inventar salários;
* não inventar tecnologias;
* não apresentar informações externas como se estivessem na base;
* e informar quando determinada informação não está disponível.

Por exemplo, se o usuário pergunta qual empresa possui a melhor cultura organizacional, o sistema não tenta deduzir isso a partir do salário ou das tecnologias. Ele informa que esse dado não existe na base.

---

## 6. Como desenvolvi — 35 segundos

Para desenvolver o projeto, primeiro criei uma **base fictícia com 20 vagas**, contendo informações como cargo, empresa, área, nível, modalidade, salário e tecnologias.

Depois desenvolvi a camada de consulta utilizando **Python e Pandas**, responsável pelos filtros, contagens, médias e ordenações.

Em seguida, implementei a integração com um **LLM local utilizando Ollama**, para transformar os resultados estruturados em respostas naturais.

Também criei prompts com regras específicas de comportamento e desenvolvi **testes automatizados e uma avaliação determinística** para verificar se os resultados calculados pelo sistema estavam corretos.

---

## 7. Resultado e fechamento — 20 segundos

Na avaliação final, foram executados **14 casos de avaliação**, cobrindo consultas, filtros combinados, médias, maiores salários e situações em que a informação não estava disponível.

Além disso, os testes automatizados apresentaram **8 testes aprovados**.

Então, mais do que um chatbot, o CareerAdvisor representa uma aplicação de IA em que eu procurei combinar **dados estruturados, processamento determinístico e inteligência artificial generativa**, mantendo o modelo dentro dos limites das informações realmente disponíveis.

Esse é o principal objetivo do CareerAdvisor: **transformar dados de vagas em respostas úteis, sem abrir mão da confiabilidade.**

Obrigada!
