from app.main import is_isogram


def test_playgrounds_is_true() -> None:
    assert is_isogram("playgrounds") is True


def test_look_is_false() -> None:
    assert is_isogram("look") is False


def test_adam_is_false() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_long_word() -> None:
    assert is_isogram("alphabet") is False


def test_is_isogram_is_false() -> None:
    assert is_isogram("is_isogram") is False
