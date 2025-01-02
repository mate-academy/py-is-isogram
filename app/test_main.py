import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "initial_word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("local", False)
    ]
)
def test_is_isogram(initial_word: str, expected_result: bool) -> None:
    assert is_isogram(initial_word) == expected_result
