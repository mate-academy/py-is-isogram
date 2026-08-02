from app.main import is_isogram


def test_should_return_false_if_the_same_letters_are_in_row() -> None:
    assert is_isogram("qwwerty") is False


def test_return_false_if_case_is_different_letters_are_repeated() -> None:
    assert is_isogram("CocaCola") is False


def test_should_return_true_if_word_is_empty() -> None:
    assert is_isogram("") is True


def test_should_return_false_if_same_letter_different_case() -> None:
    assert is_isogram("Cc") is False


def test_should_return_true_if_all_correct() -> None:
    assert is_isogram("qwerty") is True
