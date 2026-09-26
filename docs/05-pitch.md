# 05 — Pitch

Olá! Eu sou Maria Eduarda e este é o CareerAdvisor, um assistente virtual desenvolvido com IA Generativa para ajudar na exploração de oportunidades profissionais em tecnologia.

O problema é que informações de vagas podem ser difíceis de comparar. O usuário pode encontrar várias oportunidades, mas ter dificuldade para identificar tecnologias, níveis, modalidades e faixas salariais presentes na base.

O CareerAdvisor combina dados estruturados e um modelo de linguagem local. As vagas ficam em CSV e são consultadas com Python e Pandas. Os resultados relevantes são transformados em contexto e enviados para um modelo Llama executado localmente pelo Ollama.

O modelo não deve inventar respostas: ele recebe os dados encontrados pela aplicação e deve declarar quando a base não possui informação suficiente.

Por exemplo, podemos perguntar quantas vagas exigem Python, quais tecnologias aparecem em determinada área ou qual é o salário médio de vagas com uma tecnologia.

Também existem casos de avaliação para verificar aderência aos dados, relevância e segurança.

Assim, temos um assistente local, reproduzível e focado em combinar análise de dados com IA Generativa de forma fundamentada.
