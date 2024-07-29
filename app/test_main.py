from app.main import is_isogram


def test_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_little_letter() -> None:
    assert is_isogram("look") is False


def test_big_letter() -> None:
    assert is_isogram("Adam") is False
