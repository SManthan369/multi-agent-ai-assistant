def __init__(self):

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)
