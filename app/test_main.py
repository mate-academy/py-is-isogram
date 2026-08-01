import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Alphabet", False),
        ("machine", True),
        ("eleven", False),
        ("Subdermatoglyphic", True),
        ("Dermatoglyphics", True),
        ("Noon", False),
        ("background", True),
        ("downstream", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
