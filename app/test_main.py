from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Aa") is False
    assert is_isogram("bB") is False
    assert is_isogram("Macmilan") is False


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("apple") is False
    assert is_isogram("sweet") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("radar") is False
    assert is_isogram("level") is False


def test_isogram_word_lower_case() -> None:
    assert is_isogram("lumberjack") is True
    assert is_isogram("background") is True


def test_isogram_word_mixed_case() -> None:
    assert is_isogram("Machine") is True
    assert is_isogram("Subdermatoglyphic") is True
