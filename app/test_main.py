import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("aba", False),
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Machine", True),
        ("moOse", False),
        ("uncopyrightable", True),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
