from .data_loader import load_jobs
from .data_query import query_context
from .prompts import SYSTEM_PROMPT
from .llm import ask_ollama

class CareerAdvisor:
    def __init__(self):
        self.df = load_jobs()

    def context(self, question):
        return query_context(self.df, question)

    def answer(self, question):
        context = self.context(question)
        prompt = SYSTEM_PROMPT.format(context=context, question=question)
        return ask_ollama(prompt)
