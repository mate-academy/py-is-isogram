from app.main import is_isogram


def test_words_without_repetitive_letters() -> None:
    assert (is_isogram("playgrounds") is True)


def test_words_with_repetitive_letters() -> None:
    assert (is_isogram("look") is False)


def test_words_with_big_letters() -> None:
    assert (is_isogram("Adam") is False)


def test_empty_line() -> None:
    assert (is_isogram("") is True)
