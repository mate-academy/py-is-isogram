import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, boolean",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("elephant", False),
        ("aa", False),
    ],
)
def test_is_isogram(word: str, boolean: bool) -> None:
    assert is_isogram(word) is boolean
