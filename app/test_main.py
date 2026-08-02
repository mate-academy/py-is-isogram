from app.main import is_isogram


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_mixed_different_cases() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
