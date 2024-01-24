import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,boolean_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "'playgrounds' is isogram and should return True",
        "'look' is not isogram and should return False",
        "'Adam' is not isogram and should return False",
        "Empty string should return True",
    ]
)
def test_is_isogram(word: str, boolean_result: bool) -> None:
    assert is_isogram(word) == boolean_result
