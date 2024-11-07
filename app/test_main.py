from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics") == True
    assert is_isogram("moOse") == False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") == True


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("alphabet") == False

def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("hello") == False
