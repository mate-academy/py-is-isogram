from app.main import is_isogram


def test_is_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_non_isogram() -> None:
    assert is_isogram("look") is False


def test_mixed_isogram() -> None:
    assert is_isogram("Adam") is False
