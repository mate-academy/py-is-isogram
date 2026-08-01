from app.main import is_isogram


def test_should_return_true_for_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_word_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_should_return_false_for_case_insensitive_duplicates() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_single_letter_word() -> None:
    assert is_isogram("A") is True


def test_should_return_true_for_mixed_case_unique_letters() -> None:
    assert is_isogram("Python") is True


def test_should_return_false_for_repeated_letters_non_consecutive() -> None:
    assert is_isogram("banana") is False
