import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, result",
    [
        ("", True),
        ("a", True),
        ("ah", True),
        ("dog", True),
        ("isogram", True),
        ("subdermatoglyphic", True),
        ("hydromagnetics", True),
        ("palindrome", True),
        ("goo", False),
        ("civil", False),
        ("radar", False),
        ("totalitarianism", False),
        ("Uraguay", False),
        ("Monticello", False),
        ("google", False),
        ("systemic", False),
        ("booger", False),
        ("letter", False),
        ("supercalifragilisticexpialidocious", False),
        ("Adam", False),
        ("McDonalds", False),
        ("WORLD", True),
        ("BOOLEAN", False),
        ("bookkeeper", False),
        ("mississippi", False),
        ("aaaaa", False),
        ("Bb", False),
        ("qwertyuiiopasdfghjkzxcvbnm", False),
        ("zxcvbnmasdfghjkqwertyi", True),
        ("asdfghjkaqwertyuizxcvmnb", False),
        ("AbCdEfGhIa", False),
        ("aA", False),
        ("AbA", False),
        ("ADAM", False),
        ("hello", False),
        ("HELLO", False),
        ("A", True),
        ("Z", True),
        ("ab", True),
        ("AB", True),
        ("aB", True),
        ("abcabc", False),
        ("level", False)
    ]
)
def test_is_isogram(string: str, result: bool) -> None:
    assert is_isogram(string) == result
