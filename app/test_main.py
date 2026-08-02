from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert (
        is_isogram("") is True
    ), "test_empty_string_is_isogram"


def test_function_is_case_insensitive() -> None:
    assert (
        is_isogram("AadertYG") == is_isogram("aaDERtYg")
    ), "function_is_case_insensitive"


def test_non_consecutive_and_consecutive_repeated_letters_is_not_isogram(
) -> None:

    assert (
        is_isogram("look") == is_isogram("kolo") is False
    ), "non_consecutive_and_consecutive_repeated_letters_is_not_isogram"
