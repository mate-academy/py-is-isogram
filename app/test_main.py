import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Beach", True)
    ],
    ids=[
        "look should return False",
        "`Adam` should return False",
        "Empty string should return True",
        "Beach should return true"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word) == result)
