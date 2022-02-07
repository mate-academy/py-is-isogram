from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_letters_spaces_symbols():
    assert is_isogram("abc .,?:!") is True


def test_mixed_cases_letters():
    assert is_isogram("Scarf") is True


def test_same_letters_of_different_cases():
    assert is_isogram("Test") is False


def test_long_string_with_repeated_letters():
    assert is_isogram("independence") is False
