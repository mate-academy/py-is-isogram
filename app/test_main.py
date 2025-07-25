from app.main import is_isogram


def test_empty_str_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_is_isogram() -> None:
    assert is_isogram("abc") is True


def test_consecutive_letters_not_isogram() -> None:
    assert is_isogram("aaaaaaaaa") is False


def test_non_consecutive_letters_not_isogram() -> None:
    assert is_isogram("abcda") is False


def test_is_case_insensitive() -> None:
    assert is_isogram("aA") is False
