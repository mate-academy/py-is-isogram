from app.main import is_isogram


def test_isogram_with_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_isogram_empty_string() -> None:
    assert is_isogram("") is True
