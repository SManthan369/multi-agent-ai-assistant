from unittest.mock import MagicMock, patch

from tools.web_search import web_search


@patch("tools.web_search.DDGS")
def test_web_search_returns_results(mock_ddgs):

    mock_instance = MagicMock()

    mock_instance.__enter__.return_value.text.return_value = [
        {
            "title": "Python",
            "href": "https://python.org",
            "body": "Python Official Website"
        }
    ]

    mock_ddgs.return_value = mock_instance

    results = web_search("Python")

    assert len(results) == 1
    assert results[0]["title"] == "Python"
    assert results[0]["url"] == "https://python.org"
    assert results[0]["body"] == "Python Official Website"


@patch("tools.web_search.DDGS")
def test_web_search_empty_results(mock_ddgs):

    mock_instance = MagicMock()

    mock_instance.__enter__.return_value.text.return_value = []

    mock_ddgs.return_value = mock_instance

    results = web_search("abcdefxyz")

    assert results == []


@patch("tools.web_search.DDGS")
def test_web_search_exception(mock_ddgs):

    mock_instance = MagicMock()

    mock_instance.__enter__.return_value.text.side_effect = Exception(
        "Network Error"
    )

    mock_ddgs.return_value = mock_instance

    results = web_search("Python")

    assert results == []