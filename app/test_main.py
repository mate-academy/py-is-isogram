from app.main import is_isogram


def test_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_none() -> None:
    assert is_isogram("") is True


def test_non_consecutive() -> None:
    assert is_isogram("look") is False
