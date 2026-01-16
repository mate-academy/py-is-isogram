import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        None,
        False,
        [1],
        (1),
        1.1
    ]
)
def test_should_take_only_str(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)


def test_should_be_case_insensitive() -> None:
    assert (
        is_isogram("playgrounds") == is_isogram("PlayGrounds")
    ), "Function should work case-insensitive"


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_work_correctly(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), "Result is not as expected"
