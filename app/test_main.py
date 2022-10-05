from app.main import is_isogram


def test_if_string_empty() -> None:
    assert is_isogram('') is True


def test_with_repeating_consecutive_letters() -> None:
    assert is_isogram('look') is False


def test_with_repeating_in_different_cases() -> None:
    assert is_isogram('Adam') is False


def test_with_non_repeating_letters() -> None:
    assert is_isogram('playgrounds') is True