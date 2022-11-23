from app.main import is_isogram


def test_that_checks_case_sensitive_letters() -> None:
    assert is_isogram("Aaron") is False


def test_that_checks_if_word_is_isogram() -> None:
    assert is_isogram("John") is True


def test_that_checks_if_word_is_not_isogram() -> None:
    assert is_isogram("Penelope") is False


def test_to_check_if_empty_string_is_isogram() -> None:
    assert is_isogram("") is True
