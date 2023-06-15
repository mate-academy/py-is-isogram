from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_non_consecutive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_different_cases() -> None:
    assert is_isogram("AaAa") is False
