from app.main import is_isogram


def test_should_return_true_for_isogram_word() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("world") is True


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Success") is False


def test_should_return_false_for_non_isogram_word() -> None:
    assert is_isogram("look") is False
    assert is_isogram("alphabet") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_single_letter_word() -> None:
    assert is_isogram("A") is True
    assert is_isogram("z") is True


def test_should_return_false_when_letters_are_consecutive() -> None:
    assert is_isogram("balloon") is False
