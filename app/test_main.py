import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("NIOcean", False),
        ("wrong", True),
        ("brother", True),
        ("Ukraine", True),
        ("", True)
    ]
)
def test_is_program(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
