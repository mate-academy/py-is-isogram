from app import main


def test_isogram_returns_true_for_empty_string() -> None:
    assert main.is_isogram("") is True


def test_isogram_returns_true_for_word_with_unique_letters() -> None:
    assert main.is_isogram("playgrounds") is True


def test_isogram_returns_false_for_word_with_consecutive_duplicate_letters(
) -> None:
    assert main.is_isogram("look") is False


def test_isogram_returns_false_for_word_with_non_consecutive_duplicate_letters(
) -> None:
    assert main.is_isogram("alphabet") is False


def test_isogram_is_case_insensitive() -> None:
    assert main.is_isogram("Adam") is False
