LATEST_KEYWORDS = [
    "latest",
    "today",
    "current",
    "news",
    "2026",
    "recent",
    "new",
    "update",
    "live",
    "released"
]


def should_use_web_search(query: str) -> bool:
    """
    Decide whether the query needs live web information.
    """

    query = query.lower()

    for keyword in LATEST_KEYWORDS:
        if keyword in query:
            return True

    return False