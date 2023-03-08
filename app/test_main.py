from app.main import is_isogram


def test_word_is_isogram() -> None:
    assert is_isogram('fork') is True


def test_empty_string_is_isogram() -> None:
    assert is_isogram('') is True


def test_word_is_not_isogram() -> None:
    assert is_isogram('request') is False


def test_word_with_different_letters_cases_is_not_isogram() -> None:
    assert is_isogram('rEquest') is False


def test_work_with_same_consecutive_letters_is_not_isogram() -> None:
    assert is_isogram('look') is False
