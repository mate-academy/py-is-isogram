from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_repeated_insensitive():
    assert is_isogram("QWERTYUIOPP") is False


def test_repeated_sensitive():
    assert is_isogram("asdfghjkll") is False


def test_core_functionality():
    assert is_isogram("sldkfjrjfdmo") is False
    assert is_isogram("asdfghjk09865") is True
