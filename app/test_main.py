import app.main as main


def test_isogram_true() -> None:
    assert main.is_isogram("playgrounds") is True
    assert main.is_isogram("Dermatoglyphics") is True
    assert main.is_isogram("subdermatoglyphic") is True


def test_isogram_false() -> None:
    assert main.is_isogram("look") is False
    assert main.is_isogram("banana") is False
    assert main.is_isogram("abcdea") is False
    assert main.is_isogram("aabbcc") is False


def test_case_insensitive() -> None:
    assert main.is_isogram("Aa") is False
    assert main.is_isogram("AbBa") is False
    assert main.is_isogram("ABcdefg") is True


def test_empty_string() -> None:
    assert main.is_isogram("") is True


def test_non_consecutive_duplicates() -> None:
    assert main.is_isogram("abca") is False
    assert main.is_isogram("abcABC") is False


def test_consecutive_duplicates() -> None:
    assert main.is_isogram("aabbcc") is False
    assert main.is_isogram("aA") is False
