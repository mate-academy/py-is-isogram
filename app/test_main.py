from app.main import is_isogram


def test_string_with_different_cases_same_letter_is_not_an_isogramr() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_if_given_empty_string() -> None:
    assert is_isogram("") is True


def test_not_only_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("look") is False


def test_not_only_non_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("garage") is False
