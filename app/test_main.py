from app.main import is_isogram


def test_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_not_isogram() -> None:
    assert is_isogram("look") is False


def test_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_srting() -> None:
    assert is_isogram("") is True
