from app.main import is_isogram


def test_is_isogram_should_return_bool_type() -> None:
    assert isinstance(is_isogram(""), bool)


def test_is_isogram_for_an_empty_string_should_be_true() -> None:
    assert is_isogram("") is True


def test_is_isogram_non_consecutive_letters_prevent_isogram() -> None:
    assert is_isogram("look") is False


def test_is_isogram_should_all_letters_in_the_word_is_unique() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_should_verify_that_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False
