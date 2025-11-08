import os

DEBUG = True
HOST = "0.0.0.0"
PORT = 5000
MODEL_NAME = "distilbert-base-uncased-distilled-squad"

CONTEXT_FILE = os.path.join("data", "context.txt")
DEFAULT_CONTEXT = """
ChatGPT is an advanced AI language model developed by OpenAI.
It can understand natural language, generate responses, and assist in various tasks such as answering questions, writing code, or explaining concepts.
"""

def load_context():
    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return DEFAULT_CONTEXT
