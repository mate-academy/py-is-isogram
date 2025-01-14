from app.main import is_isogram


def test_empty_string():
    assert is_isogram('') == True

def test_single_letter():
    assert is_isogram('a') == True

def test_isogram_lowercase():
    assert is_isogram('playgrounds') == True

def test_not_isogram_repeated_letters():
    assert is_isogram('look') == False

def test_isogram_mixed_case():
    assert is_isogram('Playgrounds') == True

def test_not_isogram_mixed_case():
    assert is_isogram('Adam') == False

def test_isogram_special_characters():
    assert is_isogram('abCDefG') == True

def test_not_isogram_with_spaces():
    assert is_isogram('hello world') == False

def test_not_isogram_repeated_letters_different_cases():
    assert is_isogram('Test') == False

# Edge cases
def test_long_isogram():
    assert is_isogram('abcdefghijklmnopqrstuvwxyz') == True

def test_long_non_isogram():
    assert is_isogram('abcdefghijklmnopqrstuvwxyza') == False
