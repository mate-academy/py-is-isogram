import app.main as main


def test_word_without_repeating_letters() -> None:
    assert main.is_isogram("playgrounds") is True


def test_word_with_consecutive_repeating_letters() -> None:
    assert main.is_isogram("look") is False


def test_word_with_non_consecutive_repeating_letters() -> None:
    assert main.is_isogram("eleven") is False


def test_case_insensitive_word() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_one_letter_word_is_isogram() -> None:
    assert main.is_isogram("a") is True
