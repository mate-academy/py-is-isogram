from app.main import is_isogram


def test_empty_string_is_true():
    assert is_isogram("") is True


def test_upper_lower_case():
    assert is_isogram("Mm") is False


def test_words_examples():
    assert is_isogram('playgrounds') is True
    assert is_isogram('look') is False
    assert is_isogram('Adam') is False
