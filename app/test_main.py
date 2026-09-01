from app.main import is_isogram


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_word_with_repeated_letters_different_case() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_repeated_letter_non_consecutive() -> None:
    assert is_isogram("banana") is False


def test_word_with_all_unique_letters_different_case() -> None:
    assert is_isogram("AbCdEf") is True
