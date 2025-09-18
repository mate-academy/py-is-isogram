from app.main import is_isogram


def test_is_isogram_with_playgrounds() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_look() -> None:
    assert is_isogram("look") is False


def test_is_isogram_with_adam() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True
