import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("lamp", True),
        ("Letter", False),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("Aa", False),
    ],
)
def test_is_isogram(
    word: str,
    expected: bool,
) -> None:
    assert main.is_isogram(word) is expected
