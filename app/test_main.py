from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("Q", True),
        ("Aab", False)
    ]
)
def test_correct_result(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
