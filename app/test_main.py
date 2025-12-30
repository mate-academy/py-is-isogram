import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="playgrounds"),
        pytest.param("look", False, id="look"),
        pytest.param("Adam", False, id="Adam"),
        pytest.param("", True, id="empty_string"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
