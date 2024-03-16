import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected", [
        ("aaa", False),
        ("", True),
        ("Atest", False),
        ("ITS testing string", False),
        ("aTest", False),
        ("looking", False)
    ]
)
def test_is_program(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
