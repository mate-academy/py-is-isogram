from app.main import is_isogram


def test_empty_string():
    assert is_isogram('') is True


def test_word_with_repeating_consecutive_letters():
    assert is_isogram('apple') is False


def test_word_with_different_case_letters():
    assert is_isogram('Adam') is False


def test_word_without_repeating_letters():
    assert is_isogram('beach') is True
