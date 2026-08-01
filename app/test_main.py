from app.main import is_isogram

import pytest


def test_value_should_be_letters() -> None:
    assert (isinstance(is_isogram(""), bool))


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_check_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
