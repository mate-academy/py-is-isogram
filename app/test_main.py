from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_with_all_unique_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("goOd") is False


def test_long_isogram_word() -> None:
    assert is_isogram("background") is True


def test_single_letter_word_is_isogram() -> None:
    assert is_isogram("N") is True


def test_two_same_letters_is_not_isogram() -> None:
    assert is_isogram("bb") is False
