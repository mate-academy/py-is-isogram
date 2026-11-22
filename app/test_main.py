import pytest

import app.main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True),
        ("a", True),
        ("Aa", False)

    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert app.main.is_isogram(word) == expected
