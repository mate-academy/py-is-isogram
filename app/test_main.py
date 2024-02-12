from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("MADAM") is False


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("world") is True
    assert is_isogram("brown") is True
