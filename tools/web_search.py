from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5):
    """
    Search the web using DuckDuckGo.

    Returns:
        List of search results.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=max_results)

        for item in search_results:
            results.append({
                "title": item["title"],
                "url": item["href"],
                "body": item["body"]
            })

    return results