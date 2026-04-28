from app.main import is_isogram


def test_is_isogram_for_regular_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_for_word_with_consecutive_duplicates() -> None:
    assert is_isogram("look") is False


def test_is_isogram_for_word_with_non_consecutive_duplicates() -> None:
    assert is_isogram("apple") is False


def test_is_isogram_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_for_empty_string() -> None:
    assert is_isogram("") is True
