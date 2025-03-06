import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Play", True),
        ("DrIveN", True)
    ]
)
def test_is_word_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
