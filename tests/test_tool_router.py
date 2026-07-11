from tools.tool_router import should_use_web_search


def test_latest_news_requires_web_search():
    assert should_use_web_search("Latest AI news") is True


def test_current_weather_requires_web_search():
    assert should_use_web_search("Weather in Delhi today") is True


def test_stock_price_requires_web_search():
    assert should_use_web_search("Tesla stock price") is True


def test_general_python_does_not_require_web_search():
    assert should_use_web_search("Explain Python loops") is False


def test_machine_learning_does_not_require_web_search():
    assert should_use_web_search("What is Machine Learning?") is False
