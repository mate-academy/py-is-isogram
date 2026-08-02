import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playground", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert isinstance(word, str), (
        "Word must be a string."
    )
    assert isinstance(expected, bool), (
        "Expected result must be a boolean."
    )
    assert is_isogram(word) == expected
    assert is_isogram(word.lower()) == expected
    assert is_isogram(word.upper()) == expected
