import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_MEMORY_FILE = os.path.join(BASE_DIR, "memory", "chat_memory.json")


class MemoryManager:
    """
    Handles persistent storage of research history in a JSON file.
    """

    def __init__(self, memory_file=None):
        """
        Initialize the Memory Manager.

        Args:
            memory_file (str, optional):
                Path to the memory JSON file.
                Defaults to memory/chat_memory.json.
        """

        self.memory_file = memory_file or DEFAULT_MEMORY_FILE

        # Create memory directory if it doesn't exist
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)

        # Create or initialize the memory file
        if (
            not os.path.exists(self.memory_file)
            or os.path.getsize(self.memory_file) == 0
        ):
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def save(self, query: str, research: str):
        """
        Save a research entry to memory.
        """

        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append({"query": query, "research": research})

        # Keep only the latest 20 memories
        data = data[-20:]

        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        """
        Load all stored memories.
        """

        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def clear(self):
        """
        Clear all stored memories.
        """

        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
