from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_one_letter() -> None:
    assert is_isogram("a") is True


def test_two_same_letters() -> None:
    assert is_isogram("aa") is False


def test_string_with_different_cases() -> None:
    assert is_isogram("Aa") is False


def test_two_different_letters() -> None:
    assert is_isogram("ab") is True


def test_long_word() -> None:
    assert is_isogram("playgrounds") is True


def test_string_with_space() -> None:
    assert is_isogram("a b") is True


def test_two_words() -> None:
    assert is_isogram("one two") is False
