from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_lowercase_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_lowercase_word_with_consecutive_repeats() -> None:
    assert is_isogram("look") is False


def test_mixed_case_word_with_repeats() -> None:
    assert is_isogram("Adam") is False


def test_mixed_case_isogram() -> None:
    assert is_isogram("Machine") is True
    assert is_isogram("Subdermatoglyphic") is True


def test_lowercase_word_with_non_consecutive_repeats() -> None:
    assert is_isogram("alphabet") is False
