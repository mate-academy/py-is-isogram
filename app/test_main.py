from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_single_letter() -> None:
    assert is_isogram("a") is True


def test_is_isogram_unique_letters() -> None:
    assert is_isogram("isogram") is True


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("look") is False


def test_is_isogram_mixed_case() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_is_isogram_repeating_letters_case_insensitive() -> None:
    assert is_isogram("Alphabet") is False


def test_is_isogram_with_hyphen() -> None:
    assert is_isogram("six-year-old") is False


def test_is_isogram_with_spaces() -> None:
    assert is_isogram("lumber jack") is True
