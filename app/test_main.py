import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_output",
    [
        ("Python", True),
        ("PYTHON", True),
        ("test", False),
        ("AdAm", False),
        ("", True),
        ("A", True),
        ("a", True),
        ("Aa", False)
    ],
    ids=[
        "Capitalized Word without repeating letters",
        "Uppercase word without repeating letters",
        "Lowercase word with repeating letters",
        "Word with uppercase repeating letters",
        "Empty string",
        "Single uppercase character",
        "Single lowercase character",
        "Same letters in different cases"
    ]
)
def test_is_isogram(word: str, expected_output: bool) -> None:
    assert is_isogram(word) == expected_output
