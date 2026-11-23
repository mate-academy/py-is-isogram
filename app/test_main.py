import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_should_return_result_as_in_examples(
        word: str,
        expected: bool,
) -> None:
    assert is_isogram(word) is expected


def test_should_be_case_insensitive_for_uppercase_repeats() -> None:
    assert is_isogram("aA") is False


def test_should_be_case_insensitive_for_mixed_case_repeats() -> None:
    assert is_isogram("Moom") is False


def test_should_return_true_for_one_letter() -> None:
    assert is_isogram("a") is True


def test_should_return_false_for_consecutive_repeats() -> None:
    assert is_isogram("aab") is False


def test_should_return_false_for_non_consecutive_repeats() -> None:
    assert is_isogram("abca") is False


def test_should_return_false_when_repeat_is_at_the_end() -> None:
    assert is_isogram("abcdefgg") is False


def test_should_return_true_for_isogram_with_mixed_case() -> None:
    assert is_isogram("AbCd") is True
