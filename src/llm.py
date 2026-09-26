import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

def ask_ollama(prompt):
    payload = {"model": MODEL, "prompt": prompt, "stream": False, "options": {"temperature": 0.1}}
    response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=120)
    response.raise_for_status()
    return response.json().get("response", "").strip()
