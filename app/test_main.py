from app.main import is_isogram


def test_string_can_be_empty() -> None:
    assert is_isogram("")


def test_sting_that_has_no_repeating_letters() -> None:
    assert is_isogram("playgrounds")


def test_string_should_be_case_insensitive() -> None:
    assert not is_isogram("Adam")


def test_word_with_consecutive_but_repeating_letters_is_not_isogram() -> None:
    assert not is_isogram("apple")
