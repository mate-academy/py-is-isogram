import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("PlayGrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "should return `True`, if no repeats (case insensitive)",
        "should return `False` for lower case repeats",
        "should return `False` for different case repeats",
        "should return `True` for empty string"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) is result
