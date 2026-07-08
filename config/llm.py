from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

load_dotenv()

llm = ChatOllama(
    model=os.getenv("MODEL_NAME", "gemma2:2b"),
    temperature=0,
)