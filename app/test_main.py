import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word_lower,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Bag", True),
        ("Bagg", False),
        ("aaaaaaaaaaa", False),
        ("hide", True),
        ("hidden", False)
    ]
)
def test_is_isogram(word_lower: str, result: bool) -> None:
    assert is_isogram(word_lower) == result
