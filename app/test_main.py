from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True


def test_word_with_unique_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_reapeted_letter_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False
