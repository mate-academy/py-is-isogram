from app.main import is_isogram

def test_is_isogram_empty_string():
    assert is_isogram('') == True

def test_is_isogram_case_insensitive():
    assert is_isogram('Playgrounds') == True

def test_is_isogram_true():
    assert is_isogram('abcdefg') == True

def test_is_isogram_false():
    assert is_isogram('look') == False

def test_is_isogram_false_with_repeated_letters():
    assert is_isogram('Adam') == False
