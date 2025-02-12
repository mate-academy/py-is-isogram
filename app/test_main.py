import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("apple", False),
        ("orange", True),
        ("paper", False),
        ("", True),
        ("Rare", False)
    ]
)
def test_should_return_correct_value(word: str, result: bool) -> None:
    assert is_isogram(word) == result
