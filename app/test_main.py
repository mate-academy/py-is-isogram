import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("isogram", True),
        ("aba", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
        ("six-year-old", True),
        ("hello world", False),
        ("Hjelmqvist-Gryb-Zock-Pfund-Wax", True),
        ("Emily Jung Schwartzkopf", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
