from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected", [
    ("play", True),
    ("playa", False),
    ("", True),
    ("Adam", False),
    ("Aadm", False)
])
def test_is_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
