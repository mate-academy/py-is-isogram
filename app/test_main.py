from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_not_isogram() -> None:
    assert is_isogram("butterfly") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_if_is_case_sensitive() -> None:
    assert is_isogram("ButTerfly") is False
