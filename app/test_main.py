from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        (44, ValueError),
    ],
    ids=[
        "should return True for 'playgrounds'",
        "should return False for 'look'",
        "should return False for 'Adam'",
        "should return True for ''",
        "should return ValueError when word is not string",
    ],
)
def test_is_isogram(
    word: str,
    expected_result: bool,
) -> None:
    if not isinstance(word, str):
        with pytest.raises(ValueError):
            is_isogram(word)
    else:
        assert is_isogram(word) == expected_result
