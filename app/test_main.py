from app.main import is_isogram


def test_return_true_if_all_letters_unique() -> None:
    assert is_isogram("playgrounds") is True


def test_return_false_if_letter_not_unique() -> None:
    assert is_isogram("look") is False


def test_return_false_if_ignoring_letter_case() -> None:
    assert is_isogram("Adam") is False


def test_return_true_if_string_is_empty() -> None:
    assert is_isogram("") is True
