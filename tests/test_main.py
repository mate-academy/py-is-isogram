from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_case_insensitive():
    assert is_isogram("LKJFSDLIlsdfeojf") is False
    assert is_isogram("QWERTyuiop") is True


def test_core_functionality():
    assert is_isogram("sldkfjrjfdmo") is False
    assert is_isogram("asdfghjk09865") is True
