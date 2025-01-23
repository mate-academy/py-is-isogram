import pytest
from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_simple_isogram() -> None:
    assert is_isogram("abcde") is True


def test_non_isogram_with_consecutive_letters() -> None:
    assert is_isogram("aabbc") is False


def test_non_isogram_with_non_consecutive_letters() -> None:
    assert is_isogram("abcda") is False


def test_case_insensitive_isogram() -> None:
    assert is_isogram("AbCdE") is True


def test_case_insensitive_non_isogram() -> None:
    assert is_isogram("AbCdAa") is False


def test_another_isogram() -> None:
    assert is_isogram("zxcvbnm") is True


def test_another_non_isogram() -> None:
    assert is_isogram("programming") is False


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("abcde", True),
        ("aabbc", False),
        ("abcda", False),
        ("AbCdE", True),
        ("AbCdAa", False),
        ("zxcvbnm", True),
        ("programming", False),
    ],
)
def test_is_isogram_parametrized(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
