from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_with_unique_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_consecutive_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_word_with_non_consecutive_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("alphabet") is False


def test_check_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False
