from app.main import is_isogram


def test_empty_string():
    assert is_isogram('') is True


def test_is_isogram():
    assert is_isogram('playgrounds') is True


def test_not_isogram():
    assert is_isogram('look') is False


def test_case_insensitive():
    assert is_isogram('Adam') is False


def test_consecutive_letters_are_not_isogram():
    assert is_isogram('aab') is False
