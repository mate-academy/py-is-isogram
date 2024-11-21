from app.main import is_isogram


def test_word_is_isogram():
    assert is_isogram("playgrounds") is True


def test_word_missing():
    assert is_isogram("") is True


def test_word_is_not_isogram():
    assert is_isogram("Adam") is False
