from app.main import is_isogram


def test_is_isogram_with_isogram_word():
    assert is_isogram('playgrounds') is True

def test_is_isogram_with_repeat_word():
    assert is_isogram('look') is False

def test_is_isogram_with_insensitive():
    assert is_isogram('Adam') is False

def test_is_isogram_with_empty():
    assert is_isogram('') is True
