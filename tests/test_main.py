from app.main import is_isogram

def test_empty_string():
    assert is_isogram("") is True


def test_upper_case_letter():
    assert is_isogram("Adam") is False


def test_isogram_true():
    assert is_isogram("playgrounds") is True


def test_repeating_consecutive_letters():
    assert is_isogram("look") is False


def test_repeating_non_consecutive_letters():
    assert is_isogram("loko") is False
