from app.main import is_isogram


def test_return_true_if_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_return_false_if_letters_repeat_consecutively() -> None:
    assert is_isogram("look") is False


def test_return_false_if_letters_repeat_non_consecutively() -> None:
    assert is_isogram("Adam") is False


def test_return_true_if_word_string_is_empty() -> None:
    assert is_isogram("") is True


def test_if_function_is_case_insensitive() -> None:
    assert is_isogram("playgrounds") == is_isogram("PLAYGROUNDS")
