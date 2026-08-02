import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string_word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(string_word: str, result: bool) -> None:
    assert result == is_isogram(string_word)
