from app.main import is_isogram


def test_nothing() -> None:
    assert is_isogram("") is True


def test_has_not_repeating_letters() -> None:
    assert is_isogram("playing") is True


def test_with_repeating_letters() -> None:
    assert is_isogram("kavabanga") is False


def test_with_different_cases() -> None:
    assert is_isogram("goOd") is False


def test_with_consecutive_letters() -> None:
    assert is_isogram("good") is False
