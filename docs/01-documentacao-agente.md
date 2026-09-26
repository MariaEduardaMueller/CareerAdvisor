# 01 — Documentação do Agente

## Caso de uso
O **CareerAdvisor** é um assistente virtual com IA Generativa que ajuda a explorar uma base estruturada de vagas de tecnologia.

Ele responde sobre cargos, áreas, níveis, tecnologias, modalidades e salários disponíveis.

## Público-alvo
Estudantes e profissionais iniciantes em tecnologia que desejam explorar requisitos e padrões em um conjunto de vagas.

## Limitações
A base é um dataset de demonstração e **não representa o mercado inteiro**. O agente não inventa informações, não acessa vagas em tempo real e não recomenda uma empresa como "melhor" sem critério mensurável.

## Persona
Claro, objetivo, didático, transparente e baseado em evidências.

## Arquitetura
```text
Usuário -> Python -> Pandas -> CSV -> contexto -> prompt -> Llama/Ollama -> resposta
```

## Anti-alucinação
A aplicação consulta primeiro o CSV e monta um contexto objetivo. O Llama recebe esse contexto e uma instrução explícita para declarar insuficiência de dados quando necessário.
