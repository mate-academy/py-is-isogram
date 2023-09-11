from app.main import is_isogram


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("non") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_caps_and_lower() -> None:
    assert is_isogram("boOk") is False
