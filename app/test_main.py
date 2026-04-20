from app.main import is_isogram


def test_empty_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_without_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_same_letters() -> None:
    assert is_isogram("Adam") is False


def test_single_letter_word() -> None:
    assert is_isogram("a") is True


def test_all_unique_letters_mixed_case() -> None:
    assert is_isogram("AbCdEf") is True


def test_word_with_many_same_letters() -> None:
    assert is_isogram("letter") is False
