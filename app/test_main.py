from app.main import is_isogram


def test_empty_string() -> bool:
    assert is_isogram("") is True


def test_is_isogram_lowercase() -> bool:
    assert is_isogram("look") is False


def test_is_isogram_mixed() -> bool:
    assert is_isogram("Adam") is False
