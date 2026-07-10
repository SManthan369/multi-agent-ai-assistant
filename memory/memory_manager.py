import json
import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, "memory", "chat_memory.json")

class MemoryManager:

    def __init__(self):

        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump([], f)

    def save(self, query, research):

        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

        data.append({
            "query": query,
            "research": research
        })

        # Keep only the latest 20 memories
        data = data[-20:]

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)