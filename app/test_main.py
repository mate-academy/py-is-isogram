import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,is_word_isogram",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("playgrounds", True, id="word without repeats"),
        pytest.param("Dermatoglyphics", True, id="mixed case without repeats"),
        pytest.param("look", False, id="consecutive repeated letters"),
        pytest.param("elephant", False, id="non-consecutive repeated letters"),
        pytest.param("Adam", False, id="same letter in different cases"),
    ]
)
def test_should_check_if_word_is_isogram(
        word: str,
        is_word_isogram: bool
) -> None:
    assert is_isogram(word) is is_word_isogram
