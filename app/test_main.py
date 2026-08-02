from app.main import is_isogram


def test_isogram_word():
    assert is_isogram("isogram") is True


def test_non_isogram_word():
    assert is_isogram("door") is False


def test_empty_string():
    assert is_isogram("") is True


def test_random_long_word():
    assert is_isogram("asdyuiqweop123,/.[") is True


def test_uppercase_word():
    assert is_isogram("Arabic") is False
