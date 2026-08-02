import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("PlaygRounDs", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "check the isogram 'playgrounds'",
        "function should be case-insensitive 'PlaygRounDs'",
        "check the NOT isogram 'look'",
        "check the NOT isogram 'Adam'",
        "the empty string is an isogram ''"
    ]
)
def test_should_correctly_check_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
