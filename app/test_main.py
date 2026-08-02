from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds")


def test_is_isogram_false() -> None:
    assert not is_isogram("look")


def test_is_isogram_register() -> None:
    assert not is_isogram("Adam")


def test_is_isogram_empty() -> None:
    assert is_isogram("")
