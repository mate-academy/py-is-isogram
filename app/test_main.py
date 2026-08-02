from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),

    ]
)
def test_get_drinks_with_step(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
