from app.main import is_isogram


def test_should_return_true_for_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_word_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_false_for_non_consecutive_repeating_letters() -> None:
    assert is_isogram("alphabet") is False
