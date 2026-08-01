from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_single_letter() -> None:
    assert is_isogram("a") is True


def test_is_isogram_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_not_isogram() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_multiple_words() -> None:
    assert is_isogram("hello world") is False
