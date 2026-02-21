import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("alphabet", False),
        ("look", False),
        ("Adam", False),
        ("mArKet", True),
        ("subdermatoglyphic", True),
        ("isogram", True),
        ("aba", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
