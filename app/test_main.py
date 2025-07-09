import pytest

from app.main import is_isogram


def test_function_result_should_be_bool() -> None:
    assert isinstance(is_isogram("python"), bool)


def test_function_should_be_case_insensitive() -> None:
    assert is_isogram("WoRd") == is_isogram("word")


def test_string_with_different_cases_same_letter_is_not_an_isogram() -> None:
    assert is_isogram("WoOd") is False


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("word", True, id="`word` is isogram"),
        pytest.param("", True, id="empty string is isogram"),
        pytest.param("look", False, id="`look` is not an isogram"),
        pytest.param("fantastic", False, id="`fantastic` is not an isogram"),
    ],
)
def test_function_should_work_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result
