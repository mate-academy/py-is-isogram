from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_with_different_cases() -> None:
    assert is_isogram("AsdJ") is True


def test_not_isogram_with_different_cases() -> None:
    assert is_isogram("AjkaJ") is False


def test_not_isogram_with_consecutive_letters() -> None:
    assert is_isogram("Look") is False
