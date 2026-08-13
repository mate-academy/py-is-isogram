from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_all_unique() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_consecutive() -> None:
    assert is_isogram("look") is False


def test_repeated_non_consecutive() -> None:
    assert is_isogram("Alphabet") is False


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("abcABC") is False


def test_all_same_letter() -> None:
    assert is_isogram("aaa") is False
