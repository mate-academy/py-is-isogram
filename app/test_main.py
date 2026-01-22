import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True
                     , id="long word string witch return True"),
        pytest.param("look", False
                     , id="short word return False when consecutive"),
        pytest.param("Adam", False,
                     id="short word return False when non-consecutive"),
        pytest.param("", True, id="empty string"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
