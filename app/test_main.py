import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_function_should_return_valid_boolean_value(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result


@pytest.mark.parametrize(
    "word",
    [
        "bingo",
    ]
)
def test_function_should_be_case_insensitive(word: str) -> None:
    assert is_isogram(word.upper()) == is_isogram(word.lower())
