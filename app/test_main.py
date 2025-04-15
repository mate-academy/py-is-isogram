import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("telephone", False),
        ("Adam", False),
        ("absolute", True),
        ("ACTIVE", True),
        ("ACCESS", False)
    ]
)
def test_function_is_case_insensitive(word: str, result: bool) -> None:
    assert is_isogram(word) == result

def test_function_should_return_true_when_get_empty_string() -> None:
    assert is_isogram("") == True

def test_function_get_consecutive_letter() -> None:
    assert is_isogram("accept") == False

def test_function_get_non_consecutive_letter() -> None:
    assert is_isogram("natural") == False
