from app.main import is_isogram


def test_is_isogram_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_only_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("abcd") is False
