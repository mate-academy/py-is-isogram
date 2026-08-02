from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_playgrounds_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_adam_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_single_char() -> None:
    assert is_isogram("a") is True


def test_mixed_case_unique() -> None:
    assert is_isogram("AbCdE") is True


def test_long_with_repeat() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyza") is False
