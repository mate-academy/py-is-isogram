from app.main import is_isogram


def test_word_is_isogram() -> None:
    assert is_isogram('fork') is True


def test_empty_string_is_isogram() -> None:
    assert is_isogram('') is True


def test_word_isnt_isogram() -> None:
    assert is_isogram('request') is False
