from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("madam") is False
    assert is_isogram("MaDaM") is False


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("example") is False
    assert is_isogram("alphabet") is False
    assert is_isogram("unique") is False


def test_non_letter_characters() -> None:
    assert is_isogram("hello123") is False
    assert is_isogram("special-char") is False


def test_consecutive_repeating_letters() -> None:
    assert is_isogram("programming") is False
    assert is_isogram("Mississippi") is False


def test_non_consecutive_repeating_letters() -> None:
    assert is_isogram("repeating") is False
    assert is_isogram("successful") is False
