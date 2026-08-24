from app.main import is_isogram


def test_is_isogram_true_for_word_without_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false_for_consecutive_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_false_for_non_consecutive_repeating_letters() -> None:
    assert is_isogram("kayak") is False


def test_is_isogram_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_true_for_empty_string() -> None:
    assert is_isogram("") is True
