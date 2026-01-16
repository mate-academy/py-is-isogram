from app.main import is_isogram


def test_should_return_true_with_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_false_ignoring_letter_case() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_if_letter_appears_twice() -> None:
    assert is_isogram("look") is False


def test_should_return_true_if_all_letters_unique() -> None:
    assert is_isogram("playgrounds") is True
