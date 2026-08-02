from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Mtm") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True
