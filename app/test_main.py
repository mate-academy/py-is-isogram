from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Maks", True),
        ("Alex", True),
    ]
)
def test_is_word_a_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    "word, exception",
    [
        (123, AttributeError),
        (("Maks",), AttributeError),
        (["Alex"], AttributeError),
        (-0.1, AttributeError),
    ]
)
def test_exception_if_word_not_string(word: str, exception: Exception) -> None:
    with pytest.raises(exception):
        is_isogram(word)
