import pytest
from app import main


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_simple_isogram() -> None:
    assert main.is_isogram("abcde") is True


def test_non_isogram_with_consecutive_letters() -> None:
    assert main.is_isogram("aabbc") is False


def test_non_isogram_with_non_consecutive_letters() -> None:
    assert main.is_isogram("abcda") is False


def test_case_insensitive_isogram() -> None:
    assert main.is_isogram("AbCdE") is True


def test_case_insensitive_non_isogram() -> None:
    assert main.is_isogram("AbCdAa") is False


def test_another_isogram() -> None:
    assert main.is_isogram("zxcvbnm") is True


def test_another_non_isogram() -> None:
    assert main.is_isogram("programming") is False


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
    assert main.is_isogram(word) is expected_result


def test_isogram_is_case_insensitive() -> None:

    assert main.is_isogram("AbCdE") is True
    assert main.is_isogram("AbCda") is False
