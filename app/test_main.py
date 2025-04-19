from app.main import is_isogram


def test_valid_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_invalid_isogram_with_repeats() -> None:
    assert is_isogram("look") is False


def test_invalid_case_sensitive_repeat() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_mixed_case() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_not_isogram_with_non_consecutive_repeat() -> None:
    assert is_isogram("banana") is False


def test_valid_short_word() -> None:
    assert is_isogram("abc") is True


def test_invalid_short_word_repeat() -> None:
    assert is_isogram("aba") is False
