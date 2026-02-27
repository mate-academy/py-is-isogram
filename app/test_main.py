from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert not is_isogram("Adam")


def test_empty_string_is_isogram() -> None:
    assert is_isogram("")


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert not is_isogram("aba")


def test_consecutive_letters_are_not_isogram() -> None:
    assert not is_isogram("aa")
