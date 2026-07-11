import os
import sys
import tempfile
import pytest

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture
def temp_memory_file():
    """Temporary JSON file for MemoryManager tests."""

    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)

    yield path

    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def sample_state():
    """Reusable workflow state for agent tests."""

    return {
        "query": "Artificial Intelligence",
        "dataset": "",
        "research": "",
        "plan": "",
        "report": "",
        "analysis": "",
        "messages": [],
        "approval": True
    }