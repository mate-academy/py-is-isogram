from app.main import is_isogram


def test_empty_word():
    assert is_isogram("") is True


def test_repeating_letters():
    assert is_isogram("look") is False


def test_no_repeating_letters():
    assert is_isogram("playgrounds") is True


def test_case_sensitivity():
    assert is_isogram("Adam") is False
