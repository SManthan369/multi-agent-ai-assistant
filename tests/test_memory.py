import json

from memory.manager import MemoryManager


def test_memory_save_and_load(temp_memory_file):

    manager = MemoryManager(temp_memory_file)

    manager.save(
        "AI",
        "Artificial Intelligence Research"
    )

    memories = manager.load()

    assert len(memories) == 1
    assert memories[0]["query"] == "AI"
    assert memories[0]["research"] == "Artificial Intelligence Research"