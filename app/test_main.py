from typing import Any

import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("a", True, id="single letter is an isogram"),
        pytest.param(
            "playgrounds", True,
            id="word without repeating letters is an isogram"
        ),
        pytest.param(
            "subdermatoglyphic", True,
            id="long word without repeating letters is an isogram"
        ),
        pytest.param(
            "look", False,
            id="word with consecutive repeating letters is not an isogram"
        ),
        pytest.param(
            "Adam", False,
            id="word with non-consecutive repeating letters "
               "is not an isogram"
        ),
        pytest.param(
            "Mm", False,
            id="the same letter in different cases is not an isogram"
        ),
        pytest.param(
            "abcdea", False,
            id="word repeating its first letter at the end "
               "is not an isogram"
        ),
    ]
)
def test_should_detect_isogram(word: str, expected_result: bool) -> None:
    assert main.is_isogram(word) is expected_result


@pytest.mark.parametrize(
    "word",
    [
        pytest.param(5, id="integer raises AttributeError"),
        pytest.param(None, id="none raises AttributeError"),
        pytest.param(["a", "b"], id="list raises AttributeError"),
    ]
)
def test_should_raise_attribute_error_on_wrong_data_type(word: Any) -> None:
    with pytest.raises(AttributeError):
        main.is_isogram(word)
