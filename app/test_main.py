import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("aA", False),
        ("aa", False),
        ("background", True),
        ("ada", False),
        ("AbC", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    ), f"The word {word} is not isogram."
