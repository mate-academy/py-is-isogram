from app.main import is_isogram


def test_empty_input():
    assert is_isogram('') is True


def test_only_one_letters():
    assert is_isogram('playgrounds') is True


def test_repeated_letters():
    assert is_isogram('look') is False


def test_uppercase_letter():
    assert is_isogram('Adam') is False
