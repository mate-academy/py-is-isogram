import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("qwertyuiop", True),
        ("asdfghjkl", True),
        ("zxcvbnm", True),
        ("", True)
    ]
)
def test_should_return_true(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("rruujhjh", False),
        ("wwwww", False),
        ("qqqqqqqq", False)
    ]
)
def test_should_return_false(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
