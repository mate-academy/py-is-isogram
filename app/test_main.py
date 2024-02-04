import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "The 'playgrounds' should return True",
        "The 'look' should return False",
        "The 'Adam' should return False",
        "The '' should return True"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
