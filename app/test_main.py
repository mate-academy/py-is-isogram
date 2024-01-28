from app.main import is_isogram


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_consecutive_word() -> None:
    assert is_isogram("abcdefa") is False


def test_non_consecutive_word() -> None:
    assert is_isogram("playgrounds") is True


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_mixed_case_non_isogram() -> None:
    assert is_isogram("Mm") is False
