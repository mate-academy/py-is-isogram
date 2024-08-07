from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_upper_letter() -> None:
    assert is_isogram("Adam") is False


def test_repeat_letter() -> None:
    assert is_isogram("look") is False


def test_no_repeat_letter() -> None:
    assert is_isogram("playgrounds") is True
