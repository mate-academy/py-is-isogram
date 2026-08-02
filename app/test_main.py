from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_with_no_repeating_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True


def test_word_with_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False
    assert is_isogram("hello") is False


def test_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Dermatoglyphic") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True
