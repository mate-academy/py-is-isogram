from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters_consecutive() -> None:
    assert is_isogram("look") is False


def test_repeated_letters_non_consecutive() -> None:
    assert is_isogram("alphabet") is False


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False  # 'A' == 'a'


def test_single_letter() -> None:
    assert is_isogram("A") is True
