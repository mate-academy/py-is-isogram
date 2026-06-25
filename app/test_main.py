from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics") is True, "String with different cases of the same letter is not an isogram."


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True, "Empty string is an isogram."


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aba") is False, "Not only consecutive letters are not an isogram."


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aa") is False, "Not only non-consecutive letters are not an isogram."
