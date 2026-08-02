from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("abc") is True
    assert is_isogram("aacd") is False


def test_is_isogram_with_upper_latter() -> None:
    assert is_isogram("Abcd") is True
    assert is_isogram("aAcD") is False
    assert is_isogram("abcCda") is False


def test_is_isogram_without_letter() -> None:
    assert is_isogram("") is True


def test_is_isogram_with_long_string() -> None:
    assert is_isogram("nhjfwvgfghbwejfkvevwnUIGYUGHGGYVWfwk") is False
    assert is_isogram("qwertyuiopASDFGHJ") is True


def test_is_isogram_with_one_upper_latter() -> None:
    assert is_isogram("A") is True


def test_is_isogram_with_repeated_letter() -> None:
    assert is_isogram("aaa") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("abcdeaf") is False
