from app.main import is_isogram

def test_empty_string_is_isogram():
    assert is_isogram("") == True

def test_non_consecutive_letters_are_not_isogram():
    assert is_isogram('habanera') == False

def test_isogram_is_case_insensitive():
    assert is_isogram('Adam') == False

def test_consecutive_letters_are_not_isogram():
    assert is_isogram('look') == False
