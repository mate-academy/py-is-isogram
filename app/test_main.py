import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("AaAAAaaaa", False),
    ("", True),
    ("acegikmoqsuwy", False),
    ("abcdefghijklmnopqrstuvwxyz", False),
])
def test_is_isogram(word, expected) -> None:
    assert is_isogram(word) == expected
