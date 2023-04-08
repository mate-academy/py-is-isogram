from app.main import is_isogram
import pytest
from typing import Type


@pytest.mark.parametrize(
    "word,result",
    [
        ("title", False),
        ("Title", False),
        ("litter", False),
        ("litTer", False),
        ("playgrounds", True),
        ("", True)
    ],
    ids=[
        "non-consecutive of the same case",
        "non-consecutive of different case",
        "consecutive of the same case",
        "consecutive of different case",
        "no double letters",
        "word is empty string"
    ]
)
def test_is_isogram_returns_correct_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word,expected_error",
    [
        (25, AttributeError),
        (("l", "m"), AttributeError),
        (["l", "l"], AttributeError)
    ],
    ids=[
        "raises type error if word is number",
        "raises type error if word is tuple",
        "raises type error if word is list"
    ]
)
def test_is_isogram_returns_correct_error(
        word: str,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
