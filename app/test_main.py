import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("", True, id="empty string"),
        pytest.param("a", True, id="single letter"),
        pytest.param("abc", True, id="simple isogram"),
        pytest.param("playgrounds", True, id="long isogram"),
        pytest.param("look", False, id="repeated letter"),
        pytest.param("aba", False, id="repeated a"),
        pytest.param("Adam", False, id="case intensitive repeat"),
        pytest.param("moOse", False, id="case intensitive mix repeat"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
