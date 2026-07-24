from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_consecutive_duplicates() -> None:
    assert is_isogram("look") is False


def test_non_consecutive_duplicates() -> None:
    assert is_isogram("aba") is False


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False
