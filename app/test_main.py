from app.main import is_isogram


def test_is_isogram_with_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_is_isogram_with_mixed_case_isogram_word() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_with_single_letter_word() -> None:
    assert is_isogram("a") is True


def test_is_isogram_with_repeating_letters() -> None:
    assert is_isogram("hello") is False
