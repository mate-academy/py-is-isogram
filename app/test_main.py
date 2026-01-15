from app.main import is_isogram


def test_string_with_different_cases_of_the_same_letter_is_not_an_isogram(
) -> None:
    assert is_isogram("Adam") is False


def test_not_only_consecutive_letters_are_not_an_isogram(
) -> None:
    assert is_isogram("oops") is False


def test_not_only_non_consecutive_letters_are_not_an_isogram(
) -> None:
    assert is_isogram("look") is False


def test_empty_string_is_an_isogram(
) -> None:
    assert is_isogram("") is True
