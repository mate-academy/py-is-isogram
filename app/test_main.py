import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", True),
        ("background", True),
        ("subdermatoglyphic", True),
        ("ankyloblephAron", False),
        ("Dodle", False),
        ("Hello", False),
        ("Mississippi", False)
    ]
)
def test_check_word_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
