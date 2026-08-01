from app.main import is_isogram


# write your code here
def test_that_big_letter_eaquel_to_small_letter() -> None:
    assert is_isogram("AbC") is True
    assert is_isogram("AbCAbC") is False


def test_is_isogram_for_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_for_consecutive_letters() -> None:
    assert is_isogram("Abc") is True
    assert is_isogram("Abca") is False


def test_is_isogram_for_not_consecutive_letters_with_empty_string() -> None:
    assert is_isogram("Abc") is True
    assert is_isogram("AaBbCc") is False
