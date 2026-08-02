from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False
