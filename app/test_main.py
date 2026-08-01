import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram_word, result_isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_word_is_isogram(isogram_word: str, result_isogram: bool) -> None:
    result = is_isogram(isogram_word)
    assert result == result_isogram
