from app.main import is_isogram


def test_all_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_all_uppercase() -> None:
    assert is_isogram("PLAYGROUNDS") is True


def test_mixed_cases() -> None:
    assert is_isogram("bItE") is True


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_same_letter_in_different_cases() -> None:
    assert is_isogram("beforE") is False


def test_consecutive_letters() -> None:
    assert is_isogram("look") is False
