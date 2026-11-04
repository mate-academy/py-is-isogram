from app.main import is_isogram


def test_word_without_repeats():
    assert is_isogram("playgrounds") is True


def test_word_with_consecutive_repeats():
    assert is_isogram("look") is False


def test_word_with_repeats_in_different_case():
    assert is_isogram("Adam") is False


def test_empty_string():
    assert is_isogram("") is True
