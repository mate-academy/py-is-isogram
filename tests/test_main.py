from app.main import is_isogram


def test_when_string_is_empty():
    assert is_isogram("") is True


def test_repeated_letters_in_upper_case():
    assert is_isogram("Adam") is False


def test_repeated_letters_in_lower_case():
    assert is_isogram("look") is False


def test_not_repeated_letters():
    assert is_isogram("PlAygrOunDs") is True


def test_all_is_not_repeated_in_lower_case():
    assert is_isogram('qwertyuiop') is True
