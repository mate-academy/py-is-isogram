import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("a", True),
        ("on", True),
        ("Adam", False),
        ("look", False),
        ("playground", True),
        ("ViviennE", False)
    ]
)
def test_if_the_function_works_correctly(
        word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


def test_if_the_function_raises_exception_if_word_is_empty() -> None:
    with pytest.raises(ValueError):
        is_isogram("")


@pytest.mark.parametrize(
    "word",
    [
        4,
        3.5,
        False,
        True
    ]
)
def test_if_the_function_raises_exception_if_word_is_not_string(
        word: int | bool | float) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)


"""
1. Test czy funkcja działa poprawnie:
    "a", "on", "Adam", "look", "playgrounds", "vivienne"
2. Co jeśli word będzie puste - ValueError
3. Test czy zgłosi błąd, jeśli word nie będzie typu string - TypeError
"""
