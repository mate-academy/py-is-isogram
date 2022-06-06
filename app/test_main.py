from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_case_insensitive():
    assert is_isogram('Adam') is False


def test_string_with_no_repeating_letters():
    assert is_isogram('playgrounds') is True


def test_string_with_repeating_letter():
    assert is_isogram('look') is False
