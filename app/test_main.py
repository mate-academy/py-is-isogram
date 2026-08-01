import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,boolean",
    [
        ("word", True),
        ("Adam", False),
        ("penny", False),
        ("penNy", False),
        ("", True),
    ],
    ids=[
        "lowercase_word",
        "non_consecutive",
        "lowercase_penny",
        "uppercase_penny",
        "empty"
    ]
)
def test_is_isogram(word: str, boolean: bool) -> None:
    assert is_isogram(word) == boolean
