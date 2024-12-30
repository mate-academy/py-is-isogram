from app.main import is_isogram


def test_base_word() -> None:
    assert is_isogram("playgrounds") is True


def test_base_word_negative() -> None:
    assert is_isogram("look") is False


def test_case_if_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
