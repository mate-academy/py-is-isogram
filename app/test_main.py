from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, value",
    [
        ("", True),
        ("isogram", True),
        ("eleven", False),
        ("subdermatoglyphic", True),
        ("Alphabet", False),
        ("thumbscrew-japingly", True),
        ("book", False)

    ]
)
def test_is_isogram(word: str, value: bool) -> None:
    assert is_isogram(word) == value
