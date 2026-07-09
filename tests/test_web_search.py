from tools.web_search import web_search


results = web_search("Latest AI news")

for result in results:
    print("=" * 50)
    print(result["title"])
    print(result["url"])
    print(result["body"])