from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5):
    """
    Search the web using DuckDuckGo.

    Returns:
        List of dictionaries containing:
        - title
        - url
        - body
    """

    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for item in search_results:
                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("href", ""),
                    "body": item.get("body", "")
                })

    except Exception:
        # Return empty list if search fails
        return []

    return results