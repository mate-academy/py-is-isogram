import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True),
        ("LinkinPark", False)
    ],
    ids=[
        "empty string is_isogram",
        "lower case is_isogram",
        "upper case is_isogram",
        "unique letters is_isogram",
        "mixed case is_isogram"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
