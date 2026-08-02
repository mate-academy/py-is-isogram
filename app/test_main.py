from app.main import is_isogram


def test_different_case_letter_are_not_isogram() -> None:
    assert is_isogram("Mm") is False


def test_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_not_only_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("aaaaa") is False


def test_not_only_non_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("abababab") is False
