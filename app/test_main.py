from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False


def test_empty_word() -> None:
    assert is_isogram("") is True


def test_single_char() -> None:
    assert is_isogram("a") is True


def test_all_same() -> None:
    assert is_isogram("aaa") is False
