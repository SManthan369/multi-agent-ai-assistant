LATEST_KEYWORDS = [
    # Time-sensitive
    "latest",
    "today",
    "current",
    "recent",
    "new",
    "news",
    "update",
    "updates",
    "live",
    "released",
    # Years
    "2025",
    "2026",
    "2027",
    # Finance
    "stock",
    "stock price",
    "share price",
    "market",
    "price",
    "crypto",
    "bitcoin",
    # Weather
    "weather",
    "forecast",
    "temperature",
    # Sports
    "score",
    "match",
    "fixture",
    "result",
    # Politics
    "election",
    "government",
    # Technology
    "launch",
    "announcement",
    "version",
    "release",
]


def should_use_web_search(query: str) -> bool:
    """
    Return True if the query requires live web information.
    """

    query = query.lower().strip()

    return any(keyword in query for keyword in LATEST_KEYWORDS)
