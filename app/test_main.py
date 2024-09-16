from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_is_not_isogram_with_upper_chars():
    assert is_isogram("DYnamoKyiv") is False


def test_non_consecutive_is_not_isogram():
    assert is_isogram("abcdefa") is False
