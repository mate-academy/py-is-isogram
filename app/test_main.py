from app.main import is_isogram


def test_isogram_string() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_not_isogram_string() -> None:
    assert is_isogram("zaz") is False


def test_case_sensitive() -> None:
    assert is_isogram("lL") is False
