import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("alphabet", False),
        ("Abba", False),
        ("moOse", False),
        ("isogram", True)
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
