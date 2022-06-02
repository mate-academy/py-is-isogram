from app.main import is_isogram


def test_word_isogram():
    assert is_isogram("playgrounds") is True


def test_word_not_isogram():
    assert is_isogram("look") is False


def test_word_with_big_letters():
    assert is_isogram('Adam') is False


def test_is_empty():
    assert is_isogram('') is True
