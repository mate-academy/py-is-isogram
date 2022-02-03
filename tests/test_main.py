from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") is True


def test_mixed_letters():
    assert is_isogram("AsdfgTkl") is True
    assert is_isogram("KjhgFsrT") is True


def test_repeating_letters():
    assert is_isogram("QwWpP") is False
    assert is_isogram("PopopPO") is False
