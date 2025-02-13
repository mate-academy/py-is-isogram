from app.main import is_isogram


def test_playgrounds() -> None:
    assert is_isogram("playgrounds") is True


def test_look() -> None:
    assert is_isogram("look") is False


def test_adam() -> None:
    assert is_isogram("Adam") is False


def test_none() -> None:
    assert is_isogram("") is True
