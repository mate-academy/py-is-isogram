from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False
