from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram('') is True


def test_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_non_lowercase() -> None:
    assert is_isogram("look") is False


def test_non_isogram_mixedcase() -> None:
    assert is_isogram("Adam") is False


def test_isogram_mixedcase() -> None:
    assert is_isogram("Word") is True
