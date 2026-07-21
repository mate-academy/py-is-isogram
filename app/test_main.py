from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_without_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False  # 'a' appears twice
    assert is_isogram("Python") is True  # no repeating letters


def test_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("A") is True


def test_word_with_multiple_repeating_letters() -> None:
    assert is_isogram("hello") is False  # 'l' appears twice
    assert is_isogram("Mississippi") is False  # multiple repeating letters
