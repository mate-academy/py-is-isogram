from app.main import is_isogram


def test_with_playgrounds_should_return_true() -> None:
    assert is_isogram("playgrounds") is True


def test_with_look_should_return_false() -> None:
    assert is_isogram("look") is False


def test_with_adam_should_return_false() -> None:
    assert is_isogram("Adam") is False


def test_without_letters_should_return_true() -> None:
    assert is_isogram("") is True
