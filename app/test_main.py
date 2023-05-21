import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected", [
        pytest.param("", True, id="Empty string is an isogram"),
        pytest.param("playground", True, id="Isogram as no letters repeats"),
        pytest.param("look", False, id="Is not isogram as letters repeat"),
        pytest.param("Adam", False, id="Is not case sensitive")
    ]
)
def test_check_if_word_has_no_repeating_letters(
        word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word, expected_error", [
        pytest.param(
            [], AttributeError, id="Input value should be string, not list"),
        pytest.param(
            3, AttributeError, id="Input should be string not integer")
    ]
)
def test_check_for_input_value(word: str, expected_error: Any) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
