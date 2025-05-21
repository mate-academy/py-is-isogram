from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    isogram = is_isogram("")
    assert isogram


def test_is_isogram_false() -> None:
    isogram = is_isogram("hello world")
    assert not isogram


def test_is_isogram_true() -> None:
    isogram = is_isogram("bartek")
    assert isogram


def test_isogram_case_insensitive() -> None:
    isogram = is_isogram("WoRlD")
    assert isogram


def test_non_consecutive_letters_are_not_isogram() -> None:
    isogram = is_isogram("pytest")
    assert not isogram


def test_consecutive_letters_are_isogram() -> None:
    isogram = is_isogram("hello")
    assert not isogram
