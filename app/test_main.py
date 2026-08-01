from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_valid_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_repeating_letters_consecutive() -> None:
    assert is_isogram("look") is False


def test_repeating_letters_non_consecutive() -> None:
    assert is_isogram("banana") is False


def test_case_insensitive_false() -> None:
    assert is_isogram("ADam") is False


def test_case_insensitive_true() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_single_letter() -> None:
    assert is_isogram("A") is True


def test_two_same_letters_different_case() -> None:
    assert is_isogram("Aa") is False


def test_long_isogram() -> None:
    assert is_isogram("subdermatoglyphic") is True
