import pytest

from app.main import is_isogram


def test_should_return_true_on_empty_word() -> None:
    assert is_isogram(""), (
        "Function should return true on empty word"
    )


@pytest.mark.parametrize(
    "word,result",
    [
        ("boOl", False),
        ("Adam", False),
        ("Pip", False)
    ]
)
def test_should_be_case_insensitive(word: str, result: bool) -> None:
    assert is_isogram(word) == result, (
        "Function should be case insensitive"
    )


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("keyboard", True),
        ("listen", True)
    ]
)
def test_should_check_isogram_words(word: str, result: bool) -> None:
    assert is_isogram(word), (
        "Function should check isogram words"
    )
