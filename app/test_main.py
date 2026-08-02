from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_simple_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_non_consecutive_repeating_letters() -> None:
    assert is_isogram("aba") is False


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_all_unique_letters() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
