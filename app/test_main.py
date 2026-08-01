import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("isogram", True),
        ("Alphabet", False),
        ("Password", False),
        ("uncopyrightable", True),
        ("add", False),
        ("George", False),
        ("upstairs", False)
    ]
)
def test_is_isogram_logic(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
