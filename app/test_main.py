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
        "Playgrounds is isogram should return True",
        "Look is not isog`  ram should return False",
        "Adam is not isogram should return False",
        "The empty string is isogram should return True",
    ]
)
def test_check_if_is_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
