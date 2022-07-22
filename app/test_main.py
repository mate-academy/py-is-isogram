from app.main import is_isogram


def test_empty():
    assert is_isogram('') is True


def test_word_with_repeating_letters():
    assert is_isogram('look') is False


def test_word_with_no_repeating_letters():
    assert is_isogram('playgrounds') is True


def test_word_with_upper_case_letters():
    assert is_isogram('Adam') is False
