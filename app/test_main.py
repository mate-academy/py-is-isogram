from app.main import is_isogram

def test_empty_string_is_isogram():
    word = ""
    assert is_isogram(word) == True

def test_isogram_lowercase():
    word = "isogram"
    assert is_isogram(word) == True

def test_isogram_uppercase():
    word = "ISOGram"
    assert is_isogram(word) == True

def test_non_isogram():
    word = "hello"
    assert is_isogram(word) == False  # Виправлено порівняння

def test_mixed_case_isogram():
    word = "AbCdEfG"
    assert is_isogram(word) == True

def test_non_alpha_characters():
    word = "12345"
    assert is_isogram(word) == True
