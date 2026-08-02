from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("look", False),
        ("lOok", False),
        ("Ukraine", True),
        ("AdAm", False),
        ("Fuck russia", False),
        ("Slava Ukraini!", False)
    ]
)
def test_checking_word_string_is_iso(word: str, result: bool) -> None:
    assert is_isogram(word) == result
