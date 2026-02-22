from app.main import is_isogram


def test_playgrounds_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_adam_is_not_isogram() -> None:
    assert is_isogram("Adam") is False


def test_empty_is_isogram() -> None:
    assert is_isogram("") is True
