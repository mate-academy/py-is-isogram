from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_unique_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("cat") is True
    assert is_isogram("xyz") is True


def test_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False
    assert is_isogram("hello") is False
    assert is_isogram("book") is False


def test_case_insensitive_repeating_letters() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("mOon") is False
    assert is_isogram("TeSt") is False


def test_case_insensitive_unique_letters() -> None:
    assert is_isogram("Cat") is True
    assert is_isogram("DoG") is True
    assert is_isogram("PyThOn") is True
