from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") == True


def test_case_insensitive():
    assert is_isogram("Lola") == False


def test_different_letters():
    assert is_isogram("abcdeghijkl") == True


def test_non_isogram():
    assert is_isogram("abba") == False