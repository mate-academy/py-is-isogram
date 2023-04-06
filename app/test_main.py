import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_if_result_has_right_format(word: str, expected_result: bool) -> None:
    result = is_isogram(word)
    assert (
        isinstance(result, bool)
    ), "result should be boolean"


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_if_cat_has_years(word: str, expected_result: bool) -> None:
    assert (
        is_isogram(word) == expected_result
    ), f"{word} should be {expected_result}"

