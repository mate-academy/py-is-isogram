from app.main import is_isogram


def test_word_is_empty():
    assert is_isogram('') is True


def test_word_is_correct():
    assert is_isogram('playgrounds') is True


def test_letters_should_no_repeating():
    assert is_isogram('look') is False


def test_lower_or_upper_case():
    assert is_isogram('Adam') is False
