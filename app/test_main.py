import pytest
from typing import Type
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(
        word: str,
        expected_result: bool
) -> None:
    assert (is_isogram(word) == expected_result), \
        f"Expected result for {word} - {expected_result}"


@pytest.mark.parametrize(
    "word, expected_error",
    [
        (123, AttributeError),
        (["word"], AttributeError),
        ({"word": None}, AttributeError),
    ]
)
def test_should_raise_error_if_wrong_data_type_provided(
    word: str, expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
