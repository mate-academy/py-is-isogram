from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") == True


def test_isogram_with_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") == True, "Expected isogram"


def test_non_isogram_due_to_repeating_letters() -> None:
    assert is_isogram("look") == False


def test_non_isogram_with_case_insensitivity() -> None:
    assert is_isogram("Adam") == False


def test_isogram_with_mixed_case_letters() -> None:
    assert is_isogram("Subdermatoglyphic") == True


def test_non_isogram_with_mixed_case_repeating_letters() -> None:
    assert is_isogram("Alphabet") == False
