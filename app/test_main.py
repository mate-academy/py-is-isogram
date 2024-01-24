from app.main import is_isogram


def test_word_should_be_isogram_when_word_is_empty_string() -> None:
    assert is_isogram("") is True


def test_word_should_be_isogram_when_word_has_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_word_should_not_be_isogram_when_word_has_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_word_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False
