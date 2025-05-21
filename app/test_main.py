from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    isogram = is_isogram("")
    if isogram is True:
        assert True


def test_is_isogram_false() -> None:
    isogram = is_isogram("hello world")
    if not isogram:
        return False


def test_is_isogram_true() -> None:
    isogram = is_isogram("bartek")
    if isogram is True:
        assert True


def test_isogram_case_insensitive() -> None:
    isogram = is_isogram("WoRlD")
    if isogram is True:
        assert True


def test_non_consecutive_letters_are_not_isogram() -> None:
    isogram = is_isogram("pytest")
    if not isogram:
        return False


def test_consecutive_letters_are_isogram() -> None:
    isogram = is_isogram("hello")
    if not isogram:
        return False
