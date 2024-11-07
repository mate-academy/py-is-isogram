from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("moOse") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("alphabet") is False


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("hello") is False
