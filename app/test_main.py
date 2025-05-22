from app.main import is_isogram


def test_should_return_true_for_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_word_with_consecutive_duplicates() -> None:
    assert is_isogram("look") is False


def test_should_return_false_for_word_with_non_consecutive_duplicates() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Machine") is True
    assert is_isogram("mAchine") is True
    assert is_isogram("mAcHiNe") is True
    assert is_isogram("Moo") is False


def test_should_return_true_for_single_letter_word() -> None:
    assert is_isogram("A") is True


def test_should_return_false_if_all_letters_are_same() -> None:
    assert is_isogram("aaaa") is False
