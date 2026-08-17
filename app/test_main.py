from app.main import is_isogram


def test_is_isogram_with_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_repeat_word() -> None:
    assert is_isogram("look") is False


def test_is_isogram_with_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_with_empty() -> None:
    assert is_isogram("") is True
