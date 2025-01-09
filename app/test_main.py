from app.main import is_isogram


def test_is_isogram_when_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_when_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_when_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_when_case_is_different() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_when_same_letters_case_insensitive() -> None:
    assert is_isogram("ff") is False
