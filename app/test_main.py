from app.main import is_isogram


def test_playgrounds() -> None:
    assert is_isogram("playgrounds")


def test_look() -> None:
    assert not is_isogram("look")


def test_adam() -> None:
    assert not is_isogram("Adam")


def test_empty_string() -> None:
    assert is_isogram("")
