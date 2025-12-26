from app.main import is_isogram


def test_empty_word() -> None:
    assert (is_isogram("") is True)


def test_word_with_chars_not_repeat() -> None:
    assert (is_isogram("playgrounds") is True)


def test_word_with_chars_repeated() -> None:
    assert (is_isogram("look") is False)


def test_word_with_different_char_register() -> None:
    assert (is_isogram("Adam") is False)
