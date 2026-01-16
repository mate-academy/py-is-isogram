from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_empty_string_uppercase() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_repeat_letters() -> None:
    assert is_isogram("look") is False


def test_empty_string_long_word() -> None:
    assert is_isogram("playgrounds") is True
