from app.main import is_isogram


def test_when_string_is_empty():
    assert is_isogram("") is True


def test_string_with_double_and_upper_letters():
    assert is_isogram("Adam") is False


def test_string_with_double_and_lower_letters():
    assert is_isogram("look") is False


def test_without_double_letters():
    assert is_isogram("PlAygrOunDs") is True


def test_all_lower_not_repeated():
    assert is_isogram('qwertyuiop') is True
