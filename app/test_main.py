import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="no repeating letters"),
        pytest.param("look", False, id="with repeating letters"),
        pytest.param("Adam", False, id="repeating letters case-insensitive"),
        pytest.param("", True, id="empty string"),
        pytest.param("qwe  rty z", False, id="repeating spaces"),
        pytest.param("1234 5678", True, id="string numbers")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
