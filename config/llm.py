from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

# Load environment variables
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gemma2:2b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))

llm = ChatOllama(
    model=MODEL_NAME,
    base_url=OLLAMA_HOST,
    temperature=TEMPERATURE,
)
