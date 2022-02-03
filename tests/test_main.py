from app.main import is_isogram


def test_when_string_is_empty():
    assert is_isogram("") is True


def test_string_with_upper_letters():
    assert is_isogram("Adam") is False


def test_string_with_double_letters():
    assert is_isogram("look") is False


def test_without_double_letters():
    assert is_isogram("playgrounds") is True
