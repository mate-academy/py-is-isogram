from app.main import is_isogram


def test_a_single_char() -> None:
    assert is_isogram("k") is True


def test_an_empty() -> None:
    assert is_isogram("") is True


def test_case_insensitive() -> None:
    assert is_isogram("kOmo") is False


def test_some_cases() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("fokgoerpgpoIKPOFGfpekwkvm") is False
