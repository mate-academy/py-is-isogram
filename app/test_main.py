import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("test", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("Alphabet", False),
        ("Adam", False),
    ],
    ids=[
        "word without repeating letters",
        "word with repeating letters",
        "empty string",
        "long word without repeating letters",
        "case insensitive repeated letter",
        "simple case insensitive repeated letter",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
