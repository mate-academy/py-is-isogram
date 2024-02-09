from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_with_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True, "Expected isogram"


def test_non_isogram_due_to_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_non_isogram_with_case_insensitivity() -> None:
    assert is_isogram("Adam") is False


def test_isogram_with_mixed_case_letters() -> None:
    assert is_isogram("Subdermatoglyphic") is True


def test_non_isogram_with_mixed_case_repeating_letters() -> None:
    assert is_isogram("Alphabet") is False
