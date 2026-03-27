from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_simple_isogram() -> None:
    assert is_isogram("lamp") is True


def test_should_return_false_for_word_with_duplicate_letters() -> None:
    assert is_isogram("letter") is False


def test_should_return_false_for_non_consecutive_duplicates() -> None:
    assert is_isogram("hello") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_should_return_false_when_same_letter_in_different_cases() -> None:
    assert is_isogram("moOse") is False


def test_should_handle_long_isogram() -> None:
    assert is_isogram("subdermatoglyphic") is True


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("hello") is False


def test_repeated_letters_not_next_to_each_other() -> None:
    assert is_isogram("alphabet") is False
