from app.main import is_isogram


def test_string_empty():
    assert is_isogram("") is True


def test_with_letter_upper_case():
    assert is_isogram("Adam") is False


def test_with_letter_lower_case():
    assert is_isogram("look") is False


def test_not_repeated_letters():
    assert is_isogram("BackEnd") is True


def test_is_not_repeated_with_lower_case():
    assert is_isogram('background') is True
