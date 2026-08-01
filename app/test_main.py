from app.main import is_isogram


def test_is_isogram_playgrounds_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_look_false() -> None:
    assert is_isogram("look") is False


def test_is_isogram_adam_false() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_empty_str_true() -> None:
    assert is_isogram("") is True
