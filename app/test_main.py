from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_word_should_be_isogram():
    assert is_isogram("playgrounds") is True


def test_word_should_not_be_isogram():
    assert is_isogram("look") is False


def test_word_lover_and_uppercase():
    assert is_isogram("Adam") is False
