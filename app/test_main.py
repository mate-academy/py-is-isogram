from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True


def test_regular_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_word_with_repeating_non_consecutive_letters() -> None:
    assert is_isogram("banana") is False


def test_case_insensitive_repeat() -> None:
    assert is_isogram("Adam") is False


def test_case_insensitive_isogram() -> None:
    assert is_isogram("Alphabet".lower()) is False


def test_all_same_letter_uppercase_and_lowercase() -> None:
    assert is_isogram("Aa") is False


def test_long_isogram() -> None:
    assert is_isogram("dermatoglyphics") is True


def test_isogram_with_mixed_case_no_repeats() -> None:
    assert is_isogram("Subdermatoglyphic") is True
