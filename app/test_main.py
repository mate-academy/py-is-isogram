from app.main import is_isogram

def test_is_isogram() -> None:
    assert is_isogram("John") == True

def test_empty_is_isogram() -> None:
    assert is_isogram("") == True

def test_string_with_different_cases_is_not_isogram() -> None:
    assert is_isogram("Book") == False

def test_no_consecutive_cases_is_not_isogram() -> None:
    assert is_isogram("Eagle") == False
