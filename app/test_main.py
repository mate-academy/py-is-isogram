import pytest

from app.main import is_isogram

is_isogram_data = [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
]


@pytest.mark.parametrize("word,expection", is_isogram_data)
def test_is_isogram(word: str, expection: bool) -> None:
    assert is_isogram(word) == expection
