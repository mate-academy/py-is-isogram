import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "Kirill", False,
            id="test_with_consecutive_and_non_consecutive_repeated_letters"),
        pytest.param(
            "", True,
            id="test_empty_word_is_isogram"),
        pytest.param(
            "Water", True,
            id="test_word_without_repeated_letters"),
        pytest.param(
            "African", False,
            id="test_word_with_non_consecutive_repeated_letters"),
        pytest.param(
            "Mellon", False,
            id="test_word_with_non_consecutive_repeated_letters")
    ]
)
def test_word_is_consecutive(word: str, result: bool) -> None:
    assert (is_isogram(word) == result)
