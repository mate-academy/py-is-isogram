from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_from_date(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_type() -> None:
    assert type(is_isogram("test")) == bool
