import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("look", False, id="look"),
        pytest.param("Adam", False, id="Adam"),
        pytest.param("", True, id="word is empty"),
        pytest.param("playgrounds", True, id="playgrounds lowercase"),
        pytest.param("PLAYGROUNDS", True, id="PLAYGROUNDS uppercase"),
        pytest.param("PlAYgrOuNDs", True, id="different registers"),

    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
